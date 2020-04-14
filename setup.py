import os

from setuptools import setup

base_dir = os.path.dirname(os.path.abspath(__file__))
magic_dir = os.path.join(base_dir, 'magic')

setup(
    name='magic-msys-bin',
    version='1.1',
    py_modules=['magic_env'],
    url='https://github.com/alexsilva/magic-msys-bin',
    scripts=[],
    license='MIT',
    author='alex',
    author_email='alex@fabricadigital.com.br',
    description='magic compiled dlls for win32',
    data_files=[(
        'magic', [
            os.path.join(magic_dir, "libgnurx-0.dll"),
            os.path.join(magic_dir, "magic1.dll"),
            os.path.join(magic_dir, "magic.mgc")
        ]
    )]
)
