from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(["greeting.pyx", "compute.pyx"])
)

# criar arquivo com extensão .pyx
# python setup.py build_ext --inplace