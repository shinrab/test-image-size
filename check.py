# Check the sizes of the resized images.

from pathlib import Path

from PIL import Image

output_root = Path("resized_samples")

for size_dir in sorted(path for path in output_root.iterdir() if path.is_dir()):
    print(f"[{size_dir.name}]")
    for image_path in sorted(size_dir.glob("*.jpg")):
        with Image.open(image_path) as im:
            print(image_path.name, im.size)
