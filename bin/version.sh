#!/bin/bash

VERSION=$(python3 -c "exec(open('../seunggabi_core_python/__init__.py').read()); print(__version__)")
echo "[as-is] $VERSION"

IFS='.' read -r -a VERSION_PARTS <<< "$VERSION"
X=${VERSION_PARTS[0]}
Y=${VERSION_PARTS[1]}
Z=${VERSION_PARTS[2]}

CMD=$1
if [ -z "${CMD}" ]; then
  CMD="z"
fi

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

echo "[to-be] $X.$Y.$Z"

sed -i "s/__version__ = .*/__version__ = \"$X.$Y.$Z\"/" ../seunggabi_core_python/__init__.py
