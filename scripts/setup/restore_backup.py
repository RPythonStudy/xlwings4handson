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

    # 현재 폴더와 백업 폴더 정의 (같은 depth의 backup/{현재폴더명}-backup)
    current_dir = Path.cwd()
    backup_dir = current_dir.parent / "backup" / f"{current_dir.name}-backup"

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

    # wiki 폴더 restore: 기존 파일 중 일부를 제외하고 삭제 후 백업에서 복사
    wiki_backup = backup_dir / "wiki"
    wiki_current = current_dir / "wiki"
    preserve_files = {"Home.md", "Project-Overview.md", "Project-Setup-Guide.md", ".git"}
    if not wiki_current.exists():
        wiki_current.mkdir(parents=True, exist_ok=True)
    # 기존 파일/폴더 중 preserve_files를 제외하고 삭제
    for item in wiki_current.iterdir():
        if item.name not in preserve_files:
            try:
                if item.is_file():
                    item.unlink()
                    log_info(f"Deleted wiki file: {item}")
                elif item.is_dir():
                    shutil.rmtree(item)
                    log_info(f"Deleted wiki folder: {item}")
            except Exception as e:
                log_error(f"Failed to delete wiki item {item}: {e}")
    # 백업에서 복사 (백업이 있을 때만)
    if wiki_backup.exists():
        for item in wiki_backup.iterdir():
            if item.is_file():
                copy_item(item, wiki_current / item.name)
    else:
        log_error(f"No wiki folder in backup: {wiki_backup}")

    log_info("Backup restore completed.")

if __name__ == "__main__":

    main()

    # 운영체제와 무관하게 Zone.Identifier 파일 일괄 삭제 (Path 기반)
    deleted_count = 0
    for file_path in Path.cwd().rglob("Zone.Identifier"):
        try:
            file_path.unlink()
            log_info(f"Deleted Zone.Identifier: {file_path}")
            deleted_count += 1
        except Exception as e:
            log_error(f"Failed to delete {file_path}: {e}")
    if deleted_count:
        log_info(f"Total Zone.Identifier files deleted: {deleted_count}")
    else:
        log_info("No Zone.Identifier files found for deletion.")
