# Check the sizes of the resized images.

from pathlib import Path

from PIL import Image

for p in sorted(Path("resized_samples").glob("sample_*x*.jpg")):
    with Image.open(p) as im:
        print(p.name, im.size)
