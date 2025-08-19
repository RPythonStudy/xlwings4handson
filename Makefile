## Python 환경 및 로그 자동화 Makefile

# 1. 가상환경 생성은 가장 먼저 분리
venv:
	python scripts/setup_venv.py
	@echo "[INFO] 파이썬 가상환경이 생성되었습니다."


# 개별 실행 가능한 타겟 분리
env:
	python scripts/create_env.py
	@echo "[INFO] .env 파일 설정 완료"

log:
	python scripts/create_log_path.py
	@echo "[INFO] 로그 경로 및 파일 생성 완료"

import:
	python scripts/set_import_path.py
	@echo "[INFO] 파이썬 import 경로 설정 완료"

check:
	python scripts/check_syspath.py
	@echo "[INFO] syspath 체크 완료"

repo:
	python scripts/change_repository_url.py
	@echo "[INFO] 저장소 및 wiki 서브모듈 URL이 변경되었습니다."

restore:
	python scripts/restore_backup.py
	@echo "[INFO] 백업이 복원되었습니다."

# 전체 자동화 finalize
finalize: env log import check repo
	@echo "[INFO] 모든 설정이 완료되었습니다."

# rlib: src/rlib의 파일을 src/r로 복사
rlib:
	python scripts/copy_rlib.py
	@echo "[INFO] src/rlib의 파일이 src/r로 복사되었습니다."

