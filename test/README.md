### install
```shell
rm -rf .venv

virtualenv .venv
. .venv/bin/activate

pip3 install -r requirements.txt
```

### test
```shell
deactivate
. .venv/bin/activate

export PYTHONPATH=${PYTHONHOME}:../seunggabi_core_python && pytest --cov=../seunggabi_core_python */*.py --cov-report term-missing
```
