#! /bin/bash
set -ex

pip install -e .[dev]
pre-commit install
