"""
create_log_path.py
.env 파일에서 로그 경로를 읽어 logs 폴더 및 로그 파일을 생성
"""

from pathlib import Path
import os
from dotenv import load_dotenv

ROOT = Path.cwd()
ENV_FILE = ROOT / '.env'
if not ENV_FILE.is_file():
    print("[ERROR] .env 파일이 없습니다. 먼저 .env를 복사하세요.")
    exit(1)

load_dotenv(ENV_FILE)
service_log_path = os.getenv('SERVICE_LOG_PATH')
audit_log_path = os.getenv('AUDIT_LOG_PATH')

for log_path in [service_log_path, audit_log_path]:
    if not log_path:
        print(f"[WARN] 로그 경로가 .env에 정의되어 있지 않습니다: {log_path}")
        continue
    log_dir = Path(log_path).parent
    if not log_dir.is_dir():
        log_dir.mkdir(parents=True, exist_ok=True)
        print(f"[INFO] logs 폴더 생성: {log_dir}")
    else:
        print(f"[INFO] 이미 폴더 존재: {log_dir}")
