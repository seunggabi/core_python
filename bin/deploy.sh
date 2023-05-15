#!/bin/bash

cd ..

rm -rf dist
rm -rf build
rm -rf seunggabi_core_python.egg-info

python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*
