from setuptools import setup, find_packages

import seunggabi_core_python

from seunggabi_core_python.util import dependency_util

setup(
    name="seunggabi_core_python",
    version=seunggabi_core_python.__version__,
    description="A collection of core Python modules",
    author="seunggabi",
    author_email="seunggabi@gmail.com",
    url="https://github.com/seunggabi/core_python",
    packages=find_packages(),
    install_requires=dependency_util.get(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
