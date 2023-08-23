#!/bin/bash

deactivate
rm -rf .venv

virtualenv .venv
. .venv/bin/activate

pip3 install -r requirements.txt
