# [core_python](https://pypi.org/project/seunggabi-core-python/)

### install
```shell
deactivate
rm -rf .venv

python3 -m venv .venv
source .venv/bin/activate

pip3 install requests
pip3 install -r requirements.txt
```
```shell
pip3 install -r requirements.txt
```

### build
```shell
source .venv/bin/activate

cd bin

sh version.sh y
sh tag.sh 1
sh deploy.sh
```
