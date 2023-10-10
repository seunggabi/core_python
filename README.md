# [core_python](https://pypi.org/project/seunggabi-core-python/)

### install
```shell
deactivate
rm -rf .venv

virtualenv .venv
. .venv/bin/activate

pip3 install -r requirements.txt
pre-commit install
```
```shell
pip3 install -r requirements.txt
```

### build
```shell
. .venv/bin/activate

cd sh

sh version.sh z
sh tag.sh 1
sh deploy.sh
```
