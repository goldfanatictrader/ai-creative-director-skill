# Official Sources

Checked September 2026.

## Cameras
- ARRI ALEXA 265 — https://www.arri.com/en/cine-systems/cine-cameras/alexa-265
- ARRI ALEXA 35 — https://www.arri.com/en/camera-systems/cameras/alexa-35
- Sony VENICE 2 — https://pro.sony/ue_US/products/digital-cinema-cameras/venice2
- RED V-RAPTOR XL [X] — https://www.reddigitalcinema.com/v-raptor-xl-x-black
- Panavision DXL2 — https://www.panavision.com/camera-and-optics/optics/product-detail/dxl2-millennium-dxl2
- Blackmagic URSA Cine 17K 65 — https://www.blackmagicdesign.com/products/blackmagicursacine/techspecs
- Canon EOS C400 — https://www.usa.canon.com/support/p/eos-c400
- DJI Ronin 4D — https://www.dji.com/ronin-4d/specs
- Vision Research Phantom — https://www.phantomhighspeed.com/
- Phase One — https://www.phaseone.com/
- Hasselblad X2D II 100C — https://www.hasselblad.com/x-system/x2d-ii-100c
- Fujifilm GFX100 II — https://www.fujifilm-x.com/
- Leica — https://leica-camera.com/
- Panasonic LUMIX S1RII — https://www.panasonic.com/
- Panavision Millennium XL2 — https://www.panavision.com/camera-and-optics/cameras/product-detail/pfxmxl-millennium-xl2
- IMAX film-camera program — https://investors.imax.com/

## Lenses
- ARRI Signature — https://www.arri.com/en/cine-lenses/signature-lenses
- Cooke S8/i FF — https://cookeoptics.com/lens/s8-i-ff/
- ZEISS Supreme Prime Radiance — https://www.zeiss.com/photonics-and-optics/en/cinematography/lenses/supreme-prime-radiance-lenses.html
- Leitz HUGO — https://www.leitz-cine.com/product/hugo
- Panavision Primo 70 — https://www.panavision.com/camera-and-optics/optics/product-detail/4p-primo-70
- Vantage Hawk — https://www.vantagefilm.com/
- Angénieux Optimo Ultra 12x — https://www.angenieux.com/lenses/optimo-ultra-12x/

## Film
- Kodak Motion Picture Films — https://www.kodak.com/en/motion/products/

Interpretive words such as organic, clinical, humanistic, dreamlike, premium, or dimensional are directorial heuristics, not objective specifications.
## Color Management Standards Sources

Checked September 2026.

## ACES 2

- ACES Documentation — Getting Started  
  https://docs.acescentral.com/

- About ACES 2  
  https://docs.acescentral.com/background/about-aces-2/

- ACES 2 Rendering Transform  
  https://docs.acescentral.com/background/about-rendering/

Important verified notes:
- ACES is an industry-standard, open color-management framework covering capture through mastering/archive.
- ACES 2 introduces redesigned rendering/output transforms.
- ACES 2 documentation describes a gentler highlight rolloff, reduced midtone contrast versus ACES 1 output behavior, and improved gamut mapping.

## DaVinci Resolve

- Blackmagic Design — DaVinci Resolve Color  
  https://www.blackmagicdesign.com/products/davinciresolve/color

- Blackmagic Design — DaVinci Resolve Training  
  https://www.blackmagicdesign.com/products/davinciresolve/training

Important verified notes:
- Resolve supports wide-gamut and HDR workflows.
- Resolve supports its own color-management system and ACES.
- Resolve exposes input, timeline/working, and output color-management concepts.
- Resolve supports ST.2084/PQ and HLG-related HDR workflows.

## HDR

- ITU-R BT.2100-3  
  https://www.itu.int/rec/R-REC-BT.2100

Verified:
- BT.2100-3 is in force (approved February 2025).
- BT.2100 specifies two HDR systems: PQ and HLG.

## PQ

- SMPTE ST 2084 is the Perceptual Quantizer EOTF used in PQ HDR workflows.
- ITU BT.2100 incorporates PQ as one of its HDR methods.

## Dolby Vision

- Dolby Vision for Content Creators  
  https://professional.dolby.com/content-creation/dolby-vision-for-content-creators/

- Dolby Vision Professional Tools  
  https://professionalsupport.dolby.com/s/dolby-vision-professional-tools

- Dolby Vision Mastering & QC FAQs  
  https://professionalsupport.dolby.com/s/article/Master-QC-using-Dolby-Vision-FAQs

Verified:
- Dolby describes Dolby Vision mastering as beginning with an HDR master using PQ and P3 or Rec.2020 working/output gamut context.
- Dolby Vision uses dynamic metadata for mapping to target displays.
- Dolby's workflow includes analysis and optional creative trim adjustments.
- Dolby provides tools for metadata inspection/validation and mezzanine workflows.

## Interpretation Policy

The following are creative/directorial heuristics, not standards:
- "cinematic"
- "organic"
- "luxury"
- "nostalgic"
- "clinical"
- "soft highlight"
- "dense blacks"
- "warm skin"

These terms require explicit visual definition before implementation.
