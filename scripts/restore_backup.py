#!/usr/bin/env python3
# ==============================================
# scripts/restore_backup.py
# ==============================================

import os
import shutil
from pathlib import Path

# src/common/logger.py 의 함수 임포트
from common.logger import log_info, log_error

def copy_item(src: Path, dst: Path):
    """파일 또는 폴더 복사 (덮어쓰기)"""
    try:
        if src.is_dir():
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
            log_info(f"Directory restored: {dst}")
        elif src.is_file():
            shutil.copy2(src, dst)
            log_info(f"File restored: {dst}")
        else:
            log_error(f"Not found: {src}")
    except Exception as e:
        log_error(f"Failed to restore {src} -> {dst}: {e}")

def main():
    # 현재 폴더와 백업 폴더 정의
    current_dir = Path.cwd()
    backup_dir = current_dir.parent / f"{current_dir.name}-backup"

    if not backup_dir.exists():
        log_error(f"Backup folder not found: {backup_dir}")
        return

    log_info(f"Restoring backup from {backup_dir} to {current_dir}")

    # 복사 대상 디렉토리 (기존 + 추가)
    restore_dirs = [
        "data", "posts", "templates", "archive", "logs", "make", "polices", "tests", "example", "dev", "docker",
        "raw_data", "source"
    ]
    for d in restore_dirs:
        copy_item(backup_dir / d, current_dir / d)

    # 프로젝트 루트의 *.png, *.yml 파일 복사
    for ext in [".png", ".yml"]:
        for item in backup_dir.glob(f"*{ext}"):
            copy_item(item, current_dir / item.name)

    # config 폴더 내 모든 파일 복사 (logging.yml 외 추가)
    config_backup = backup_dir / "config"
    config_current = current_dir / "config"
    if config_backup.exists():
        if not config_current.exists():
            config_current.mkdir(parents=True, exist_ok=True)
        for item in config_backup.iterdir():
            if item.is_file():
                copy_item(item, config_current / item.name)
    else:
        log_error(f"No config folder in backup: {config_backup}")

    # 복사 대상 파일
    for f in ["requirements.txt", "renv.lock", "index.qmd", ".env", ".env.example"]:
        copy_item(backup_dir / f, current_dir / f)

    # src 폴더 처리
    src_backup = backup_dir / "src"
    src_current = current_dir / "src"
    if src_backup.exists():
        exclude = {"common", "R", "Rlib"}
        for sub in src_backup.iterdir():
            if sub.is_dir() and sub.name not in exclude:
                copy_item(sub, src_current / sub.name)
    else:
        log_error(f"No src folder in backup: {src_backup}")

    # wiki 폴더 내 이름이 중복되지 않는 파일 복사
    wiki_backup = backup_dir / "wiki"
    wiki_current = current_dir / "wiki"
    if wiki_backup.exists():
        if not wiki_current.exists():
            wiki_current.mkdir(parents=True, exist_ok=True)
        for item in wiki_backup.iterdir():
            if item.is_file():
                dest_path = wiki_current / item.name
                if not dest_path.exists():
                    copy_item(item, dest_path)
    else:
        log_error(f"No wiki folder in backup: {wiki_backup}")

    log_info("Backup restore completed.")

if __name__ == "__main__":

    main()

        # 운영체제와 무관하게 Zone.Identifier 파일 일괄 삭제 (파이썬 코드)
        deleted_count = 0
        for root, dirs, files in os.walk("."):
            for file in files:
                if file.endswith("Zone.Identifier"):
                    file_path = os.path.join(root, file)
                    try:
                        os.remove(file_path)
                        log_info(f"Deleted Zone.Identifier: {file_path}")
                        deleted_count += 1
                    except Exception as e:
                        log_error(f"Failed to delete {file_path}: {e}")
        if deleted_count:
            log_info(f"Total Zone.Identifier files deleted: {deleted_count}")
        else:
            log_info("No Zone.Identifier files found for deletion.")
