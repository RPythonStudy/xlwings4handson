# scripts/setup/setup_env.py
# .env.example을 복사하여 .env 생성 후, 프로젝트 폴더명과 경로 자동 치환
# _environment 파일까지 생성
# last modified: 2025-09-07
# 경로의 \ -> \\ 치환 추가

import shutil
import re
from pathlib import Path
import platform

os_name = platform.system()
print(f"운영체제: {os_name}")

ROOT = Path.cwd()
CUR_DIR_NAME = ROOT.name
src = ROOT / '.env.example'
dst = ROOT / '.env'
env_file = ROOT / '_environment'

if not src.is_file():
    print(f"[ERROR] .env.example 파일이 없습니다. 경로: {src}")
    exit(1)

shutil.copyfile(src, dst)

content = dst.read_text(encoding='utf-8')
content = re.sub(r'^PROJECT_NAME=.*', f'PROJECT_NAME={CUR_DIR_NAME}', content, flags=re.MULTILINE)
abs_path = str(ROOT)
content = re.sub(r'^PROJECT_ROOT=.*', f'PROJECT_ROOT={abs_path.replace("\\", r"\\\\")}', content, flags=re.MULTILINE)
content = content.replace('/home/ben/projects/rpy-quarto-template', abs_path)

if os_name == "Linux":
    log_path = "/var/log/{PROJECT_NAME}"
elif os_name == "Darwin":
    log_path = "$HOME/Library/Logs/{PROJECT_NAME}"
elif os_name == "Windows":
    log_path = "%USERPROFILE%\\AppData\\Local\\{PROJECT_NAME}"
else:
    log_path = "/var/log/{PROJECT_NAME}"
content = re.sub(r'^LOG_PATH=.*', f'LOG_PATH={log_path.replace("\\", r"\\\\")}', content, flags=re.MULTILINE)

dst.write_text(content, encoding='utf-8')
print("[INFO] .env 파일이 생성되고, 경로 및 프로젝트명이 현재 폴더명으로 자동 치환되었습니다.")

try:
    shutil.copyfile(dst, src)
    print("[INFO] .env.example 파일이 .env로부터 복사 생성되었습니다.")
except Exception as e:
    print(f"[ERROR] .env.example 복사 실패: {e}")

try:
    shutil.copyfile(dst, env_file)
    print("[INFO] _environment 파일이 .env로부터 복사 생성되었습니다.")
except Exception as e:
    print(f"[ERROR] _environment 복사 실패: {e}")