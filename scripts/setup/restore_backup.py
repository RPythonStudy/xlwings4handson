"""
파일명: scripts/setup/restore_backup.py
목적: data 폴더만 복원
설명: backup/<project-name>/data를 프로젝트 루트의 data로 복사
변경이력:
  - 2025-09-24: data 폴더만 복원하도록 수정 (BenKorea)
"""

from pathlib import Path
import shutil
import os
from dotenv import load_dotenv
from common.logger import log_error, log_info

def restore_data(project_root: Path):
    project_name = project_root.name
    backup_data_dir = project_root / 'backup' / project_name / 'data'
    data_dir = project_root / 'data'
    if not backup_data_dir.exists():
        log_error(f'[restore_backup.py] 백업 데이터 폴더가 존재하지 않습니다: {backup_data_dir}')
        return
    if data_dir.exists():
        shutil.rmtree(data_dir)
    shutil.copytree(backup_data_dir, data_dir)
    log_info(f'[restore_backup.py] data 폴더 복원 완료: {data_dir}')

if __name__ == "__main__":
    load_dotenv()
    project_root = os.getenv('PROJECT_ROOT')
    if not project_root:
        log_error('[restore_backup.py] PROJECT_ROOT 환경변수가 설정되어 있지 않습니다.')
    else:
        restore_data(Path(project_root))
