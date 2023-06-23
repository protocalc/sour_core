import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "sour",
    version = "1.0",
    author = "Gabriele Coppi",
    description = ("A python package for controlling Sony Cameras"),
    packages=find_packages(),
    long_description=read('README.md'),
    python_requires='>=3',
)
