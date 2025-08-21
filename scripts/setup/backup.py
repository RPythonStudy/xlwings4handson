from pathlib import Path
import shutil
import os

# 현재 프로젝트 폴더
current_dir = Path.cwd()
backup_root = current_dir.parent / "backup"
backup_dir = backup_root / f"{current_dir.name}-backup"

# 제외할 폴더
exclude = {".venv", "renv"}

# 백업 폴더 생성
backup_dir.mkdir(parents=True, exist_ok=True)

for item in current_dir.iterdir():
    if item.name in exclude:
        continue
    dest = backup_dir / item.name
    if item.is_dir():
        shutil.copytree(item, dest, dirs_exist_ok=True)
    elif item.is_file():
        shutil.copy2(item, dest)

print(f"[INFO] 백업 완료: {backup_dir}")
