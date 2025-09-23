# scripts/setup/setup_pyenv.py
# .pyenv를 인식하여 pyenv local 버전을 설정
# last modified: 2025-09-23

from pathlib import Path
import subprocess

version_file = Path(".python-version")
if version_file.exists():
    version = version_file.read_text(encoding="utf-8").strip()
    if version:
        subprocess.run(["pyenv", "local", version], check=True)
        print(f"pyenv local {version} 실행 완료")
    else:
        print(".python-version 파일이 비어 있습니다.")
else:
    print(".python-version 파일이 없습니다.")
