
from pathlib import Path
import shutil

root = Path.cwd()
src_dir = root / 'src' / 'Rlib'
dst_dir = root / 'src' / 'R'

dst_dir.mkdir(parents=True, exist_ok=True)
for src_path in src_dir.iterdir():
    if src_path.is_file():
        shutil.copy2(src_path, dst_dir / src_path.name)
