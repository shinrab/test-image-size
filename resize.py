from pathlib import Path

from PIL import Image

img = Image.open(
    "data/market1501/Market-1501-v15.09.15/bounding_box_train/0002_c2s1_068496_01.jpg"
)

sizes = [16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]

output_dir = Path("resized_samples")
output_dir.mkdir(parents=True, exist_ok=True)

for size in sizes:
    resized = img.resize((size, size), Image.BICUBIC)
    out_path = output_dir / f"sample_{size}x{size}.jpg"
    resized.save(out_path)

print(f"Resized images saved in {output_dir.resolve()}")
