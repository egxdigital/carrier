"""Carrier Setup

This module contains the setuptools.setup() definition for the Carrier program.

Usage
    source env/bin/activate
    python -m build
    deactivate
    python3.10 -m pip install --editable .
"""
import os
from pathlib import Path, PurePath
from setuptools import setup, find_packages

root = Path(__file__).resolve().parent
requirements_txt = Path(PurePath(root, 'requirements.txt'))

def read_requirements_file(fd):
    res = []
    if Path(fd).is_file():
        with open(fd, 'r') as reader:
            reqs = [lin.strip('\n')
                    for lin in reader.readlines() if '#' not in lin]
            res += [req for req in reqs if os.getenv(
                'python', '/home/engineer/source/python/projects') not in req]
    return res

with open('README.md', 'r') as fh:
    long_description=fh.read()

requirements = read_requirements_file(requirements_txt)

setup(
    name='Carrier',
    version='1.0.0',
    author='Emille Giddings',
    author_email='emilledigital@gmail.com',
    description='A tool for generating email communications.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': ['carrier=carrier.__main__:main']
    },
    tests_require=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
    setup_requires=[
        'setuptools>=42',
        'wheel',
        'setuptools_scm>=3.4',
    ],
)