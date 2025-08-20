import shutil
import os

src_dir = os.path.join('src', 'Rlib')
dst_dir = os.path.join('src', 'R')

os.makedirs(dst_dir, exist_ok=True)
for fname in os.listdir(src_dir):
    src_path = os.path.join(src_dir, fname)
    dst_path = os.path.join(dst_dir, fname)
    if os.path.isfile(src_path):
        shutil.copy2(src_path, dst_path)
