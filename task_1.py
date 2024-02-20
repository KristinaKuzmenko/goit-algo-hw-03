import argparse
from pathlib import Path
import shutil


def sort_files(path: Path, dist: Path):
    if path.exists():
        for obj in path.iterdir():
            if obj.is_dir():
                try:
                    sort_files(obj, dist)
                except Exception() as e:
                    print(f"No access to directory {obj}: {e}")
            else:
                ext = obj.suffix.lstrip(".")
                if not ext:
                    ext = "files_without_extension"
                new_path = dist / ext
                new_path.mkdir(exist_ok=True, parents=True)
                try:
                    shutil.copyfile(obj, new_path / obj.name)
                except Exception() as e:
                    print(f"Cannot copy file {obj}: {e}")
                    continue

    else:
        print("This directory doesn't exist")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=str, help="Path to the source directory.")
    parser.add_argument(
        "destination",
        type=str,
        nargs="?",
        default="dist",
        help="Path to the destination directory, default = dist",
    )

    args = parser.parse_args()
    source_path = Path(args.source)
    dest_dir = Path(args.destination)

    sort_files(source_path, dest_dir)
