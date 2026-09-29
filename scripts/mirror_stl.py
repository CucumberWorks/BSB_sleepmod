#!/usr/bin/env python3
"""Rebuild the opposite-side binary STLs using Python's standard library."""

from pathlib import Path
import math
import struct


ROOT = Path(__file__).resolve().parents[1]
PAIRS = (
    ("lightblocker_L.stl", "lightblocker_R.stl"),
    ("strap_adapter_R.stl", "strap_adapter_L.stl"),
)
TRIANGLE = struct.Struct("<12fH")


def mirror(source: Path, destination: Path) -> None:
    data = source.read_bytes()
    if len(data) < 84:
        raise ValueError(f"{source}: missing binary STL header")
    count = struct.unpack_from("<I", data, 80)[0]
    if len(data) != 84 + count * TRIANGLE.size:
        raise ValueError(f"{source}: unexpected binary STL length")

    # Reflect Y about zero. Reverse winding to keep outward-facing triangles.
    # The bracket's left/right direction lies along Y in the supplied exports.
    output = bytearray(data[:84])
    for record in TRIANGLE.iter_unpack(data[84:]):
        if not all(math.isfinite(value) for value in record[:12]):
            raise ValueError(f"{source}: non-finite coordinate or normal")
        nx, ny, nz = record[:3]
        a, b, c = (record[i:i + 3] for i in (3, 6, 9))
        output.extend(TRIANGLE.pack(
            nx, -ny, nz,
            a[0], -a[1], a[2],
            c[0], -c[1], c[2],
            b[0], -b[1], b[2],
            record[12],
        ))
    destination.write_bytes(output)
    print(f"{source.name} -> {destination.name} ({count:,} triangles)")


if __name__ == "__main__":
    for original, mirrored in PAIRS:
        mirror(ROOT / "stl" / original, ROOT / "stl" / mirrored)
