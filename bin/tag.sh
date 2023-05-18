#!/bin/bash

FORCE=$1

VERSION=$(python3 -c "exec(open('../seunggabi_core_python/__init__.py').read()); print(__version__)")
echo "[version] $VERSION"

branch=$(git symbolic-ref --short -q HEAD)
echo "[branch] $branch"

if [[ ! $FORCE && $branch != "main" ]]; then
  echo "[exception] need to main branch"
  exit 1
fi

git pull

tag="v-$VERSION"
echo "[tag] "$tag

git tag -d $tag
git push origin :$tag

git tag $tag
git push --tags

