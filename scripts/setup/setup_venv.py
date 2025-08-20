"""
setup_venv.py
OS별로 분기하여 파이썬 가상환경 생성 및 requirements.txt 설치
"""
import os
import sys
import subprocess

VENV_DIR = os.path.join(os.path.dirname(__file__), '..', '.venv')
REQUIREMENTS = os.path.join(os.path.dirname(__file__), '..', 'requirements.txt')

# 운영체제 감지
platform = sys.platform
if platform.startswith('win'):
    pip_path = os.path.join(VENV_DIR, 'Scripts', 'pip.exe')
    python_path = os.path.join(VENV_DIR, 'Scripts', 'python.exe')
    activate_cmd = f'{VENV_DIR}\\Scripts\\activate'
elif platform == 'darwin':
    pip_path = os.path.join(VENV_DIR, 'bin', 'pip')
    python_path = os.path.join(VENV_DIR, 'bin', 'python')
    activate_cmd = f'source {VENV_DIR}/bin/activate'
else:  # Linux 및 기타
    pip_path = os.path.join(VENV_DIR, 'bin', 'pip')
    python_path = os.path.join(VENV_DIR, 'bin', 'python')
    activate_cmd = f'source {VENV_DIR}/bin/activate'

# 가상환경 생성
if not os.path.isdir(VENV_DIR):
    print(f"[INFO] 가상환경 생성: {VENV_DIR}")
    subprocess.run([sys.executable, '-m', 'venv', VENV_DIR], check=True)
else:
    print(f"[INFO] 이미 가상환경 존재: {VENV_DIR}")

# requirements.txt 설치
if os.path.isfile(REQUIREMENTS):
    print(f"[INFO] requirements.txt 설치 중...")
    subprocess.run([pip_path, 'install', '-r', REQUIREMENTS], check=True)
else:
    print(f"[WARN] requirements.txt 파일이 없습니다.")

print(f"[INFO] 가상환경 활성화 명령: {activate_cmd}")
print(f"[INFO] 가상환경 파이썬 경로: {python_path}")
