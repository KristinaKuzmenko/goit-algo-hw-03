from pathlib import Path
import shutil


def sort_files(path: Path, dist="dist"):
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
                new_path = Path(dist) / ext
                new_path.mkdir(exist_ok=True, parents=True)
                try:
                    shutil.copyfile(obj, new_path / obj.name)
                except Exception() as e:
                    print(f"Cannot copy file {obj}: {e}")
                    continue

    else:
        print("This directory doesn't exist")
