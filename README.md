# core-python

### install
```shell
deactivate
rm -rf venv

python3 -m venv venv
source venv/bin/activate

pip3 install requests
pip3 install -r requirements.txt
```
```shell
pip3 install -r requirements.txt
```

### build
```shell
rm -rf dist
rm -rf build

python3 setup.py sdist bdist_wheel
```

### deploy
```shell
python3 -m twine upload dist/*
```