from   shutil import rmtree

import os

ls = os.listdir()

for d in ['directory', 'env', '__pycache__']:
    if d in ls:
        rmtree(d)

