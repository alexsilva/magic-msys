# coding: utf-8
import os
import sys

try:
    import pathlib
except ImportError:
    import pathlib2 as pathlib

script_dir = pathlib.Path(os.path.abspath(__file__)).parent

python_dir = sys.base_prefix

magic_dir = pathlib.Path(python_dir, 'magic')

if not magic_dir.is_dir():
    # in virtualenv path (external python)
    if hasattr(sys, 'real_prefix'):
        magic_dir = pathlib.Path(sys.real_prefix, "magic")
    # this is script path
    if not magic_dir.is_dir():
        magic_dir = script_dir.joinpath('magic')

_setup_loaded = False


def setup():
    """Configures the paths of the DLLs"""
    global _setup_loaded
    if _setup_loaded:
        return
    os.environ['PATH'] = os.pathsep.join([os.environ['PATH'], str(magic_dir)])
    os.environ['MAGIC'] = str(magic_dir.joinpath('magic.mgc'))
    _setup_loaded = True
