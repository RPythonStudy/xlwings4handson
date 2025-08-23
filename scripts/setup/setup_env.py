
"""
create_env.py
.env.example을 복사하여 .env 생성 후, 프로젝트 폴더명과 경로 자동 치환
"""

import shutil
import re
from pathlib import Path
import platform

os_name = platform.system()
print(f"운영체제: {os_name}")

# 프로젝트 루트 기준 경로
ROOT = Path.cwd()
CUR_DIR_NAME = ROOT.name
src = ROOT / '.env.example'
dst = ROOT / '.env'


if not src.is_file():
    print(f"[ERROR] .env.example 파일이 없습니다. 경로: {src}")
    exit(1)

shutil.copyfile(src, dst)


# 파일 내용 치환
content = dst.read_text(encoding='utf-8')
# PROJECT_NAME 치환
content = re.sub(r'^PROJECT_NAME=.*', f'PROJECT_NAME={CUR_DIR_NAME}', content, flags=re.MULTILINE)
# 경로 치환: .env.example 내 /home/ben/projects/rpy-quarto-template 또는 PROJECT_ROOT 값을 현재 폴더의 절대경로로 대체
abs_path = str(ROOT)
content = re.sub(r'^PROJECT_ROOT=.*', f'PROJECT_ROOT={abs_path}', content, flags=re.MULTILINE)
content = content.replace('/home/ben/projects/rpy-quarto-template', abs_path)

# 운영체제별 LOG_PATH 치환
if os_name == "Linux":
    log_path = "/var/log/{PROJECT_NAME}"
elif os_name == "Darwin":
    log_path = "$HOME/Library/Logs/{PROJECT_NAME}"
elif os_name == "Windows":
    log_path = "%USERPROFILE%\\AppData\\Local\\{PROJECT_NAME}"
else:
    log_path = "/var/log/{PROJECT_NAME}"
content = re.sub(r'^LOG_PATH=.*', f'LOG_PATH={log_path}', content, flags=re.MULTILINE)

dst.write_text(content, encoding='utf-8')

print("[INFO] .env 파일이 생성되고, 경로 및 프로젝트명이 현재 폴더명으로 자동 치환되었습니다.")

# .env 파일을 .env.example로 복사
try:
    shutil.copyfile(dst, src)
    print("[INFO] .env.example 파일이 .env로부터 복사 생성되었습니다.")
except Exception as e:
    print(f"[ERROR] .env.example 복사 실패: {e}")
