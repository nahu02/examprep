## Overview
This subtopic covers **how to design 3D models so they can actually be fabricated**, how **additive (e.g. FDM/FFF) vs. subtractive (CNC, laser)** methods differ, how to **tune slicer settings** for printability/strength, and how to **choose between FFF and alternative 3D printing methods** (SLA, SLS, etc.) for a given prototype.

---

## Key Concepts to Master

- **Additive manufacturing** builds objects by _joining_ material layer by layer _to form the object_.
- **Subtractive manufacturing** creates 3D objects by _cutting_ material away from a _solid_ block.
- **FFF / FDM** mainly uses _thermoplastic_ plastics such as _PLA_ and _PETG_ or _ABS_.
- **CNC** is a _subtractive manufacturing_ method that can process materials such as _metals_, _wood_, and _plastics_ _(long long list of different stuff)_.
- **Laser cutting** is a subtractive process that uses a _laser_ to cut materials, and is especially good for _intricate_ details.
- **Print orientation** affects part _stability_, surface _finish_, need for _supports_, and overall printability.
- **Common slicer parameters** you should be able to justify: layer _height_, infill _percentage_ and _pattern_, perimeter (wall) _thickness_, support _pattern_, print _orientation?_.
- **Design-for-printability guidelines**: limit unsupported _overhangs_, provide adequate wall _thickness_, consider tolerances/clearances of about _0.3_ mm for mating parts (depending on printer).
- **Alternative additive methods** to FDM/FFF: _SLA_, _SLS_ / _DMLS_, _plaster_-based 3D printing (_binder jetting_), thermal _phase change_ inkjets, and _laminated_ object manufacturing (_LOM_).
- **Fabrication method selection** should consider at least: required material _properties_, geometric _properties_, needed surface _finish_, mechanical _strength_, and time / _budget_ constraints.
- **Additive vs. subtractive for PCBs**: subtractive removes unwanted _material_ (e.g. milling, acid etching), while additive _adds_ copper (or conductive ink) only where needed.
- **Research directions in 3D prototyping** relevant to Physical Computing include: adding _new properties_ to printed objects, helping users _create_ models, and inventing new _printing_ methods.

---

## Definitions (Fill These In)

- **Additive manufacturing**: _Manufacturing process where final object is built up layer-by-layer from some material(s)_.
- **Subtractive manufacturing**: _Manufacturing process where final object is created by chipping/cutting material away from some block_.
- **Fused Deposition Modeling (FDM) / Fused Filament Fabrication (FFF)**: _Classic 3D printing method (see printers in Chomsky), where filament (some thermoplastic) is heated up and extruded layer by layer to form the final object_.
- **CNC (Computer Numerical Control)**: _SM method, where a CNC machine mills/drills/cuts excess material out from a block to carve the desired object out_.
- **Stereolithography (SLA)**: _Resin-based 3D printing, where liquid resin is solidified layer-by-layer via UV light. Produces smooth surfaces very quickly, but fumes and unsolidified resin is toxic_.
- **Selective Laser Sintering (SLS) / Direct Metal Laser Sintering (DMLS)**: _3D printing method, where base material is a powder (nylon/metal). The printer lays out a layer of the powder, heats  up (melting together) some section of it (one layer of the final object). For the next layer, the bed is lowered and a new layer of dust is put down and selectively melted. Not terribly inexpensive, objects need no external supports, waste is minimal, but post-processing excavation is needed for all printed objects. Results can be pretty tough, although metals may be more brittle than expected. You really don't want to inhale the fine dust_.
- **Plaster-based 3D printing (PP)**: _Similar method to SLS, but gypsum plaster is the base and instead of a laser, some binder (glue) is used to join the material. Can be colored with great accuracy (binder can be basically jetink printed with different colors). End results need to be excavated and treated with some resin or extra glue, because otherwise the texture is like chalk_.
- **Laminated Object Manufacturing (LOM)**: _Big roll of material is used; laser cutter-like machine cuts out each layer, then it it stuck/otherwise joined with below layers. Kind of a hybrid between AM and SM_.
- **Layer height (slicer setting)**: _Layer height is the vertical thickness of each individual layer your printer lays down. For FDM printers it ranges from .12 to .3 mm. Lower layer heights usually mean better detail but longer print times_.
- **Infill (density + pattern)**: ____________.
- **Support structures**: _Supports are temporary structures that allow the printer to handle steep angles, bridges, or floating features. (Overhangs requiring supports are usually anything > 45° from vertical.) Different slicers may generate different supports also based on the settings, but they are usually a compromise between trying to use less material and being easy to remove / trying to be more robust_.
- **Tolerances / clearance** in 3D printing: _Extra space (thickness of material or lack thereof) on models introduced specifically to counter the imprecision of the printing method_.

---

## Important Distinctions

### Additive vs. Subtractive (General)

| Aspect            | **Additive (e.g. FDM, SLA, SLS)**                                                           | **Subtractive (CNC, Laser)**                                                      |
| ----------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Basic principle   | Builds by ______ material layer by layer from ______.                                       | Removes material from a ______ block by cutting/milling/ablating.                 |
| Typical tools     | 3D printers (FDM, SLA, SLS, PP, etc.)                                                       | CNC mills, drills, lathes, laser cutters.                                         |
| Material use      | Only places material where ______ is needed; less waste.[PhysicalComputing_12_PCBs.pdf p.6] | Removes unwanted material → more ______ and waste.                                |
| Geometric freedom | Good for complex internal ______ and undercuts; limited by ______ and overhangs.[8]         | Good for 2.5D and prismatic parts; hard to make enclosed ______ without assembly. |
| Typical materials | Thermoplastics (PLA, ABS, sometimes nylon), resins, powders, etc.                           | Metals (aluminum, steel, brass, copper), wood, foam, plastics, etc.               |

### CNC vs. FDM (specifically)

| Aspect              | **CNC**                                                                     | **FDM / FFF**                                                                                              |
| ------------------- | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Method type         | ______ manufacturing.                                                       | ______ manufacturing.                                                                                      |
| Materials           | Huge variety: metal ______, woods, plastics, foams, wax.                    | Mostly thermoplastics: ______, ______, sometimes ______; composites less robust than solid machined parts. |
| Geometry limits     | Tool access, minimum tool ______, difficult internal cavities.              | Overhang angles, need for ______, layer adhesion, limited build volume.[1][5][8]                           |
| Surface + precision | Very good dimensional accuracy and surface finish (depending on machine).   | Layered surface; accuracy depends on printer and slicer settings; visible layer lines.[5][6]               |
| When better         | High-strength structural parts in metal/wood; precise flat/planar features. | Rapid prototyping for complex shapes, enclosures, internal channels, integrated electronics mounts.        |

### Laser cutter vs. CNC (subtractive tools)

- **Laser cutter**:
  - Uses a _laser_ to cut materials with very narrow _beam_.
  - Especially good for ultra-_fine_ details and 2D profiles in sheet materials.
- **CNC**:
  - Uses rotating _lathes_, mills, drills to remove material.
  - Better for 3D contoured surfaces; may struggle with ultra-_sharp_ inner corners compared to laser.

---

## Likely Exam Questions

1. **Explain additive vs. subtractive manufacturing and give one Physical Computing example for each.**  
   - Use definitions from the overview slides and PCB slides, and give examples like FDM enclosures vs. CNC/laser-cut parts.

2. **Compare CNC and FDM for producing a robust mechanical part that must withstand repeated user interaction (e.g. a button housing). Which would you choose and why?**  
   - Discuss material options, strength, precision, and waste.

3. **You need a small, detailed, smooth, and possibly transparent optical part inside an interactive device. Which additive method would you choose and why not FDM?**  
   - Contrast FDM with alternatives such as SLA, SLS, PP, etc.

4. **What are the key slicer settings you would adjust when printing a functional enclosure for electronics, and how do they affect user experience (e.g. feel, durability, aesthetics)?**  
   - Connect layer height, infill, walls, supports with UX and multimodal interaction arguments.

5. **Give an example from 3D prototyping research that adds interactivity to fabricated objects, and explain how the chosen fabrication method enables that interaction.**  
   - E.g. printed optics, interactive speakers, soft teddy bears, tactile picture books.

---

## Sources to Read

| PDF                                                           | Pages            | Why Read                                                                                                                                                                       |
| ------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **PhysicalComputing_11_3DPrototyping.pdf**                    | p.2–4            | Core overview of additive methods, list of alternative 3D printing processes beyond FDM (SLA, SLS/DMLS, PP, thermal inkjets, LOM).                                             |
| **PhysicalComputing_11_3DPrototyping.pdf**                    | p.7–8, 10, 12–13 | Subtractive methods (CNC, laser), CNC technologies, detailed CNC vs. FDM material comparison, and laser-cutter capabilities/precision.                                         |
| **PhysicalComputing_11_3DPrototyping.pdf**                    | p.16             | “Additive or Subtractive?” prompt for thinking about fabrication method selection.                                                                                             |
| **PhysicalComputing_11_3DPrototyping.pdf**                    | p.19–20, 23–26   | 3D prototyping research examples (printed optics, interactive speakers, soft teddy bears, tactile picture books) and research areas like adding interactivity to fabrications. |
| **5_Debugging Prototypes - Physical Computing 2025.pptx.pdf** | p.29             | Context for using Prusa Slic3r in class; link to hands-on practice with slicer settings.                                                                                       |
| **PhysicalComputing_12_PCBs.pdf**                             | p.5–7            | Additive vs. subtractive in PCB fabrication; reinforces core concepts and vocabulary of additive/subtractive manufacturing.                                                    |

Fill the blanks directly from these pages, and optionally supplement detailed slicer and design-guideline knowledge from standard FFF design guides and your own lab experience.