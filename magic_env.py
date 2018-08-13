import os
import re

import sys

script_dir = os.path.dirname(os.path.abspath(__file__))

python_dir = os.path.dirname(sys.executable)

magic_dirpath = os.path.join(python_dir, 'magic')

# is virtualenv and installed ?
if not os.path.isdir(magic_dirpath) and bool(re.match(".*Scripts", python_dir, re.I)):
    magic_dirpath = os.path.join(os.path.dirname(os.path.dirname(script_dir)), "magic")  # Lib\\site-packages
    if not os.path.isdir(magic_dirpath):
        magic_dirpath = os.path.join(script_dir, "magic")

_setup_loaded = False


def setup():
    """Configures the paths of the DLLs"""
    global _setup_loaded
    if _setup_loaded:
        return
    os.environ['PATH'] = magic_dirpath + os.pathsep + os.environ['PATH']
    os.environ['MAGIC'] = os.path.join(magic_dirpath, 'magic.mgc')
    _setup_loaded = True
