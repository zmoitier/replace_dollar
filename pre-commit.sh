#!/bin/bash

echo "run isort"
echo "---------"
isort .
echo ""

echo "run black"
echo "---------"
black .
echo ""

echo "run mypy"
echo "--------"
python3 -m mypy replace_dollar/
echo ""

echo "run mypy"
echo "--------"
python3 -m pylint replace_dollar/
echo ""

# echo "run pytest"
# echo "----------"
# python3 -m pytest .
# echo ""
