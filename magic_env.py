import os

import sys

python_dir = os.path.dirname(sys.executable)

magic_dirpath = os.path.join(python_dir, 'magic')

_setup_loaded = False


def setup():
    """Configures the paths of the DLLs"""
    global _setup_loaded
    if _setup_loaded:
        return
    os.environ['PATH'] = magic_dirpath + os.pathsep + os.environ['PATH']
    os.environ['MAGIC'] = os.path.join(magic_dirpath, 'magic.mgc')
    _setup_loaded = True
