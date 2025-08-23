## Python 환경 및 로그 자동화 Makefile

# 1. 가상환경 생성은 가장 먼저 분리
venv:
	python scripts/setup/setup_venv.py
	@echo "[INFO] 파이썬 가상환경이 생성되었습니다."

# 개별 실행 가능한 타겟 분리
env:
	python scripts/setup/setup_env.py
	@echo "[INFO] .env 파일 설정 완료"

logs:
	sudo $(which python) scripts/setup/create_logs.py
	@echo "[INFO] 로그 경로 및 파일 생성 완료"

syspath:
	python scripts/setup/setup_syspath.py
	@echo "[INFO] 파이썬 syspath 설정 완료"

urls:
	python scripts/setup/setup_repository_urls.py
	@echo "[INFO] 저장소 및 wiki 서브모듈 URL이 변경되었습니다."

# 나머지 자동화 setup
setup: env logs syspath urls
	@echo "[INFO] 모든 설정이 완료되었습니다."

restore:
	python scripts/setup/restore_backup.py
	@echo "[INFO] 백업이 복원되었습니다."

# rlib: src/rlib의 파일을 src/r로 복사
rlib:
	python scripts/setup/copy_Rlib.py
	@echo "[INFO] src/rlib의 파일이 src/r로 복사되었습니다."

check:
	python scripts/setup/check_syspath.py
	@echo "[INFO] syspath 체크 완료"

# backup: 현재 폴더를 backup/{폴더명}-backup으로 복사 (.venv, renv 제외)
backup:
	python scripts/setup/backup.py

# include Makefile_project