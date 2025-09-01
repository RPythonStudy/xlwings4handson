# scripts/setup/setup_venv.py
# OS별로 분기하여 파이썬 가상환경 생성 및 requirements.txt 설치
# Windows에서 CMD, PowerShell, Git Bash 모두 인식하도록 수정
# last modified: 2025-09-01

import sys
import subprocess
from pathlib import Path

ROOT = Path.cwd()
VENV_PATH = ROOT / ".venv"
REQ_PATH = ROOT / "requirements.txt"

platform = sys.platform

if platform.startswith("win"):
    pip_path = VENV_PATH / "Scripts" / "pip.exe"
    python_path = VENV_PATH / "Scripts" / "python.exe"
    activate_cmds = {
        "CMD": f"{VENV_PATH}\\Scripts\\activate.bat",
        "PowerShell": f"{VENV_PATH}\\Scripts\\Activate.ps1",
        "Git Bash": f"source {VENV_PATH}/Scripts/activate",
    }
elif platform == "darwin":
    pip_path = VENV_PATH / "bin" / "pip"
    python_path = VENV_PATH / "bin" / "python"
    activate_cmds = {
        "bash/zsh": f"source {VENV_PATH}/bin/activate",
    }
else:  # Linux 및 기타
    pip_path = VENV_PATH / "bin" / "pip"
    python_path = VENV_PATH / "bin" / "python"
    activate_cmds = {
        "bash/zsh": f"source {VENV_PATH}/bin/activate",
    }

# 가상환경 생성
if not VENV_PATH.is_dir():
    print(f"[INFO] 가상환경 생성: {VENV_PATH}")
    subprocess.run([sys.executable, "-m", "venv", str(VENV_PATH)], check=True)
else:
    print(f"[INFO] 이미 가상환경 존재: {VENV_PATH}")

# requirements.txt 설치
if REQ_PATH.is_file():
    print(f"[INFO] requirements.txt 설치 중...")
    subprocess.run([str(pip_path), "install", "-r", str(REQ_PATH)], check=True)
else:
    print(f"[WARN] requirements.txt 파일이 없습니다.")

# 안내 메시지
print("\n[INFO] 가상환경 활성화 명령:")
for shell, cmd in activate_cmds.items():
    print(f"  {shell}: {cmd}")
print(f"[INFO] 가상환경 파이썬 경로: {python_path}")
