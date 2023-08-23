#!/bin/bash

CMD=$1
if [ -z "$CMD" ]; then
  CMD="z"
fi

FILE=$2
if [ -z "$FILE" ]; then
  FILE="../seunggabi_core_python/__init__.py"
fi
echo "[cmd] $CMD"
echo "[file] $FILE"

VERSION=$(python3 -c "exec(open('../seunggabi_core_python/__init__.py').read()); print(__version__)")
echo "[as-is] $VERSION"

IFS='.' read -r -a VERSION_PARTS <<< "$VERSION"
X=${VERSION_PARTS[0]}
Y=${VERSION_PARTS[1]}
Z=${VERSION_PARTS[2]}

case "$CMD" in
    "x")
        X=$((X+1))
        Y=0
        Z=0
        ;;
    "y")
        Y=$((Y+1))
        Z=0
        ;;
    "z")
        Z=$((Z+1))
        ;;
    *)
        echo "Usage: $0 (x|y|z); version=x.y.z"
        exit 1
        ;;
esac

version=$X.$Y.$Z
echo "[to-be] $version"

awk -v old="__version__ = '$VERSION'" -v new="__version__ = '$version'" '{gsub(old, new)}1' $FILE > $FILE.tmp
mv $FILE.tmp $FILE
