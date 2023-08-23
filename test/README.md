### install
```shell
rm -rf .venv

virtualenv .venv
. .venv/bin/activate

pip3 install -r requirements.txt
```

### test
```shell
export PYTHONPATH=${PYTHONHOME}:../seunggabi_core_python && pytest */*.py
```
