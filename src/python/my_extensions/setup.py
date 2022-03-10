from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [Extension("hello", ["hello.pyx"])]

setup(
    name='hello-dist',
    version="0.0.1",
    ext_modules=cythonize(extensions),
    zip_safe=False,
)