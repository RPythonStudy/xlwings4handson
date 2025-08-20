
"""
create_env.py
.env.example을 복사하여 .env 생성 후, 프로젝트 폴더명과 경로 자동 치환
"""

import shutil
import re
from pathlib import Path

# 프로젝트 루트 기준 경로
ROOT = Path.cwd()
CUR_DIR_NAME = ROOT.name
src = ROOT / '.env.example'
dst = ROOT / '.env'

if not src.is_file():
    print("[ERROR] .env.example 파일이 없습니다.")
    exit(1)

shutil.copyfile(src, dst)

# 파일 내용 치환
content = dst.read_text(encoding='utf-8')
# PROJECT_NAME 치환
content = re.sub(r'^PROJECT_NAME=.*', f'PROJECT_NAME={CUR_DIR_NAME}', content, flags=re.MULTILINE)
# 경로 치환 (예시 경로를 현재 루트로 치환)
content = content.replace('/home/ben/projects/rpy-quarto-template/', str(ROOT) + '/')
dst.write_text(content, encoding='utf-8')

print("[INFO] .env 파일이 생성되고, 경로 및 프로젝트명이 현재 폴더명으로 자동 치환되었습니다.")

# .env 파일을 .env.example로 복사
try:
    shutil.copyfile(dst, src)
    print("[INFO] .env.example 파일이 .env로부터 복사 생성되었습니다.")
except Exception as e:
    print(f"[ERROR] .env.example 복사 실패: {e}")
