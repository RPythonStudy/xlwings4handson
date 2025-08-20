"""
setup_venv.py
OS별로 분기하여 파이썬 가상환경 생성 및 requirements.txt 설치
"""

import sys
import subprocess
from pathlib import Path

# 프로젝트 루트 기준 경로
ROOT = Path.cwd()
VENV_DIR = str(ROOT / '.venv')
REQUIREMENTS = str(ROOT / 'requirements.txt')


# 운영체제 감지 및 경로 계산 (pathlib.Path 사용)
platform = sys.platform
VENV_PATH = Path(VENV_DIR)
if platform.startswith('win'):
    pip_path = VENV_PATH / 'Scripts' / 'pip.exe'
    python_path = VENV_PATH / 'Scripts' / 'python.exe'
    activate_cmd = f'{VENV_PATH}/Scripts/activate'
elif platform == 'darwin':
    pip_path = VENV_PATH / 'bin' / 'pip'
    python_path = VENV_PATH / 'bin' / 'python'
    activate_cmd = f'source {VENV_PATH}/bin/activate'
else:  # Linux 및 기타
    pip_path = VENV_PATH / 'bin' / 'pip'
    python_path = VENV_PATH / 'bin' / 'python'
    activate_cmd = f'source {VENV_PATH}/bin/activate'


# 가상환경 생성
if not VENV_PATH.is_dir():
    print(f"[INFO] 가상환경 생성: {VENV_PATH}")
    subprocess.run([sys.executable, '-m', 'venv', str(VENV_PATH)], check=True)
else:
    print(f"[INFO] 이미 가상환경 존재: {VENV_PATH}")


# requirements.txt 설치
REQ_PATH = Path(REQUIREMENTS)
if REQ_PATH.is_file():
    print(f"[INFO] requirements.txt 설치 중...")
    subprocess.run([str(pip_path), 'install', '-r', str(REQ_PATH)], check=True)
else:
    print(f"[WARN] requirements.txt 파일이 없습니다.")

print(f"[INFO] 가상환경 활성화 명령: {activate_cmd}")
print(f"[INFO] 가상환경 파이썬 경로: {python_path}")
