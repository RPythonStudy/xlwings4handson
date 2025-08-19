from common.logger import log_info
import os
import subprocess

repo = os.path.basename(os.getcwd())
account = 'BenKorea' if repo == 'access-pet-data' else 'RPythonStudy'
url = f'git@github.com:{account}/{repo}.git'
subprocess.run(['git', 'remote', 'set-url', 'origin', url], check=True)
log_info(f"Changed remote URL to {url}")

# submodule wiki url 변경
wiki_url = f'git@github.com:{account}/{repo}.wiki.git'
subprocess.run(['git', 'submodule', 'set-url', 'wiki', wiki_url], check=True)
log_info(f"Changed submodule 'wiki' URL to {wiki_url}")
