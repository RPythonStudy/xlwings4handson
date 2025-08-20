#!/usr/bin/env python3
import sys
import os
import sysconfig
from pathlib import Path

if os.environ.get('VIRTUAL_ENV') is None:
    print("가상환경이 아닙니다. 스크립트를 중단합니다.")
    sys.exit(1)

# 1. 현재 파이썬 site-packages 위치
site_packages = Path(sysconfig.get_paths()["purelib"])


# 2. 프로젝트 루트와 src 경로 (프로젝트 루트 기준)
project_root = Path.cwd()
src_path = project_root / "src"

# 3. src 경로 검증
if not src_path.is_dir():
    sys.exit(f"[ERROR] src 경로 없음: {src_path}")

# 4. .pth 파일 생성
pth_file = site_packages / "project_paths.pth"
pth_file.write_text(str(src_path) + "\n", encoding="utf-8")

# 5. 확인 메시지
print(f"[OK] .pth 생성: {pth_file}")
print(f"[OK] 추가 경로: {src_path}")
