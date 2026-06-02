from argparse import ArgumentParser
from pathlib import Path

from PIL import Image

DEFAULT_SOURCE_DIR = Path("data/market1501/Market-1501-v15.09.15/bounding_box_train")
DEFAULT_OUTPUT_ROOT = Path("resized_samples")
DEFAULT_SIZES = [16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
RESAMPLE_BICUBIC = getattr(Image, "Resampling", Image).BICUBIC


def resize_image(image_path: Path, output_root: Path, sizes: list[int]) -> None:
    with Image.open(image_path) as img:
        for size in sizes:
            size_dir = output_root / str(size)
            size_dir.mkdir(parents=True, exist_ok=True)

            resized = img.resize((size, size), RESAMPLE_BICUBIC)
            out_path = size_dir / image_path.name
            resized.save(out_path)


def resize_dataset(
    source_dir: Path, output_root: Path, sizes: list[int], limit: int | None = None
) -> None:
    image_paths = sorted(source_dir.glob("*.jpg"))
    if limit is not None:
        image_paths = image_paths[:limit]

    if not image_paths:
        print(f"No images found in {source_dir.resolve()}")
        return

    processed = 0
    for image_path in image_paths:
        try:
            resize_image(image_path, output_root, sizes)
            processed += 1
            print(f"[{processed}/{len(image_paths)}] processed {image_path.name}")
        except Exception as exc:
            print(f"[skip] {image_path.name}: {exc}")

    print(f"Resized images saved in {output_root.resolve()}")


def parse_args() -> ArgumentParser:
    parser = ArgumentParser(
        description="Resize Market1501 images into multiple square resolutions."
    )
    parser.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--sizes", type=int, nargs="*", default=DEFAULT_SIZES)
    parser.add_argument("--limit", type=int, default=None)
    return parser


def main() -> None:
    args = parse_args().parse_args()
    resize_dataset(args.source_dir, args.output_root, args.sizes, args.limit)


if __name__ == "__main__":
    main()
