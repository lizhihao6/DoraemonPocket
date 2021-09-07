#!/usr/bin/env bash
pipreqs ../ --force
rm dist/*
python setup.py clean
python setup.py sdist bdist_wheel

pip install twine
twine upload dist/*
