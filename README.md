# BSB Sleep Mod

A comfort-focused BSB mod designed for maximum sleep comfort, using an AMVR facial interface for Quest 3 and a 25 mm Velcro strap.

**Comfort is the priority. This mod does not block light as well as other solutions.**

![CAD preview of the BSB sleep mod](docs/images/assembly-preview.png)

[Original post by @cucumberworks](https://x.com/cucumberworks/status/2104484445499887772)

## What you need

| Item | Notes |
| --- | --- |
| Printed parts | One cushion bracket, two lightblockers, and two strap adapters; see below. |
| AMVR facial interface for Quest 3 | Required for this mod. |
| Velcro tape | For the attachment areas. |
| 25 mm Velcro strap | For the head strap; cut the length to fit. |
| Superglue | For assembly. |
| 3 mm magnets | Thickness and total quantity still need to be documented. Confirm before buying. |

## Parts to print

Print **one of each file** for a complete five-part set. Both sides are included; you do not need to mirror anything in your slicer.

| Part | STL | Quantity | Recommended material |
| --- | --- | --- | --- |
| Main body / cushion bracket | [cushion_bracket.stl](stl/cushion_bracket.stl) | 1 | Tough material such as nylon or PETG |
| Left lightblocker | [lightblocker_L.stl](stl/lightblocker_L.stl) | 1 | TPU |
| Right lightblocker | [lightblocker_R.stl](stl/lightblocker_R.stl) | 1 | TPU |
| Left arm / strap adapter | [strap_adapter_L.stl](stl/strap_adapter_L.stl) | 1 | TPU |
| Right arm / strap adapter | [strap_adapter_R.stl](stl/strap_adapter_R.stl) | 1 | TPU |

### Print settings

- **Main body:** use a strong preset and high infill with a tough material such as nylon or PETG.
- **Lightblockers and arm / strap adapters:** TPU is recommended for flexibility and comfort.
- Use the original scale. STL files do not store units; these files are intended to be interpreted in millimeters.
- Choose orientation, supports, and material settings for your printer. Exact orientations, layer heights, wall counts, and infill percentages have not been specified.

The mirrored parts are reflected across the Y = 0 plane, with triangle winding corrected. The supplied exports retain their original positions; arrange and orient each part on the build plate in your slicer.

## Build notes

1. Print one of each of the five parts and remove supports or rough edges.
2. Dry-fit the bracket, paired lightblockers, paired adapters, and AMVR facial interface before using glue.
3. Check magnet fit and mating polarity before securing magnets with superglue. Magnet thickness, quantity, and exact installation positions still need confirmation.
4. Add Velcro tape at the attachment areas and fit the **25 mm Velcro strap** through the strap adapters. Adjust the length for comfort.
5. Check the finished fit and retention before use. Expect some light leakage: the design prioritizes sleep comfort.

The CAD image provides an overview. Detailed attachment locations and a step-by-step photo assembly guide are not yet included, so these notes are a starting point rather than a complete assembly manual.

## File provenance

The following files are the original, unmodified exports:

- `cushion_bracket.stl`
- `lightblocker_L.stl`
- `strap_adapter_R.stl`

`lightblocker_R.stl` and `strap_adapter_L.stl` are generated opposite-side copies. To regenerate them with Python 3, run this from the repository root:

```sh
python3 scripts/mirror_stl.py
```

The script requires no third-party packages. Mirroring preserves dimensions, but physical fit of the generated counterparts has not been independently tested.

## License

A license has not yet been selected. No additional reuse permissions are granted by this repository until a license is added.
