#!/usr/bin/env python3
from __future__ import annotations
import json, re, sys
from pathlib import Path
import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []

def fail(msg: str) -> None:
    errors.append(msg)

# Parse JSON and validate schemas as schemas.
for path in sorted((ROOT / "schemas").glob("*.json")):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(data)
    except Exception as exc:
        fail(f"{path.relative_to(ROOT)}: invalid JSON/JSON-Schema: {exc}")

# Parse YAML.
for folder in ("libraries", "templates"):
    for path in sorted((ROOT / folder).glob("*.y*ml")):
        try:
            yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception as exc:
            fail(f"{path.relative_to(ROOT)}: invalid YAML: {exc}")

# Manifest.
manifest_path = ROOT / "manifest.json"
try:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for folder in manifest.get("folders", []):
        if not (ROOT / folder).exists():
            fail(f"manifest folder missing: {folder}")
    if manifest.get("entrypoint") != "SKILL.md":
        fail("manifest entrypoint must be SKILL.md")
except Exception as exc:
    fail(f"manifest.json invalid: {exc}")

# Internal explicit file references.
ref_pattern = re.compile(r"(?P<path>(?:knowledge|workflows|evals|schemas|libraries|templates|examples|sources)/[A-Za-z0-9._-]+\.(?:md|json|ya?ml))")
for path in sorted(ROOT.rglob("*")):
    if not path.is_file() or path.suffix.lower() not in {".md", ".json", ".yaml", ".yml", ".py"}:
        continue
    text = path.read_text(encoding="utf-8")
    for match in ref_pattern.finditer(text):
        target = ROOT / match.group("path")
        if not target.exists():
            fail(f"{path.relative_to(ROOT)}: broken reference -> {match.group('path')}")

# FILE_INDEX must match tracked project files (except .git).
index_path = ROOT / "FILE_INDEX.md"
if index_path.exists():
    listed = set(re.findall(r"`([^`]+)`", index_path.read_text(encoding="utf-8")))
    actual = set()
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(".git/") or rel == "FILE_INDEX.md":
            continue
        actual.add(rel)
    expected = actual
    listed_without_self = listed - {"FILE_INDEX.md"}
    missing = sorted(expected - listed_without_self)
    extra = sorted(listed_without_self - expected)
    if missing:
        fail("FILE_INDEX missing: " + ", ".join(missing))
    if extra:
        fail("FILE_INDEX extra: " + ", ".join(extra))
else:
    fail("FILE_INDEX.md missing")

# Contract assertions preventing regression to permissive readiness schemas.
shot = json.loads((ROOT/"schemas/shot.schema.json").read_text(encoding="utf-8"))
shot_required = set(shot.get("required", []))
for key in {"shot_id","purpose","duration_s","camera","performance_requirement","reference_requirement","generation_status"}:
    if key not in shot_required:
        fail(f"shot.schema.json must require {key}")
if not shot.get("allOf"):
    fail("shot.schema.json must include readiness conditional rules")

gen = json.loads((ROOT/"schemas/generation-spec.schema.json").read_text(encoding="utf-8"))
gen_required = set(gen.get("required", []))
for key in {"model_target","shot_id","mode","prompt","duration_s","aspect_ratio","negative_constraints","generation_status"}:
    if key not in gen_required:
        fail(f"generation-spec.schema.json must require {key}")

# Template/schema contract checks.
gen_template = yaml.safe_load((ROOT/"templates/generation-spec.yaml").read_text(encoding="utf-8"))
for key in {"model_target","shot_id","mode","prompt","duration_s","aspect_ratio","negative_constraints","generation_status"}:
    if key not in gen_template:
        fail(f"templates/generation-spec.yaml missing required schema field: {key}")
if not isinstance(gen_template.get("duration_s"), (int, float)) or gen_template.get("duration_s", 0) <= 0:
    fail("templates/generation-spec.yaml duration_s must be a positive example value")

shot_template = (ROOT/"templates/shot-spec.md").read_text(encoding="utf-8")
for phrase in ["performance requirement", "reference requirement", "Continuity", "Generation Status"]:
    if phrase not in shot_template:
        fail(f"templates/shot-spec.md missing readiness concept: {phrase}")

example = (ROOT/"examples/train-platform-shot.md").read_text(encoding="utf-8")
for phrase in ["performance_requirement:", "reference_requirement:", "continuity:", "generation_status: READY"]:
    if phrase not in example:
        fail(f"examples/train-platform-shot.md not synchronized with shot schema: {phrase}")

# Prevention / final-video QA regression checks.
for required_path in [
    "knowledge/prevention-first-generation.md",
    "knowledge/animal-creature-behavior-bible.md",
    "evals/sequence-preflight.md",
    "knowledge/video-qa-bible.md",
    "workflows/final-video-qa.md",
    "evals/final-video-qa.md",
    "schemas/video-qa-report.schema.json",
    "templates/video-qa-report.yaml",
]:
    if not (ROOT / required_path).exists():
        fail(f"required prevention/QA module missing: {required_path}")

skill_text = (ROOT/"SKILL.md").read_text(encoding="utf-8")
for phrase in ["SEQUENCE PREFLIGHT", "CANONICAL ASSET LOCKS", "Native final-video QA"]:
    if phrase not in skill_text:
        fail(f"SKILL.md prevention/final-QA regression: missing {phrase}")

# Pipeline ordering regression check.
skill = (ROOT/"SKILL.md").read_text(encoding="utf-8")
a, b = skill.find("→ GENERATION STRATEGY"), skill.find("→ GENERATION SPEC")
if a < 0 or b < 0 or a > b:
    fail("SKILL.md pipeline must place GENERATION STRATEGY before GENERATION SPEC")

if errors:
    print("QA FAILED")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("QA PASSED")
