#!/bin/sh

remove_directory() {
    find . -name "$1" -type d \
        -exec echo "removing {}" \; \
        -exec rm -dr {} +
}

remove_file() {
    find . -name "$1" -type f \
        -exec echo "removing {}" \; \
        -exec rm {} +
}

case "$1" in
-c)
    remove_directory "__pycache__"

    remove_directory ".mypy_cache"
    remove_directory ".ruff_cache"

    remove_directory ".pytest_cache"
    remove_directory "htmlcov"
    remove_file ".coverage"

    for EXT in 'aux' 'bak' 'fdb_latexmk' 'fls' 'log' 'out' 'synctex.gz' 'toc'; do
        remove_file "*.$EXT"
    done
    ;;
-f)
    echo ">> run isort"
    python -m isort ./
    echo ">> run docformatter"
    python -m docformatter --in-place ./
    echo ">> run black"
    python -m black ./
    ;;
-i)
    python -m flit install --symlink --deps none --user
    ;;
-t)
    python -m mypy ./replace_dollar/
    python -m pylint ./replace_dollar/
    python -m ruff ./replace_dollar/
    python3 -m pytest ./tests/
    ;;
-u)
    python -m pip install --upgrade pip
    python -m pip install --upgrade -r requirements-dev.txt
    ;;
*)
    echo "The choice are:"
    echo "  > [-c] for cleaning the temporary files;"
    echo "  > [-f] for formatting the code;"
    echo "  > [-i] locally install replace_dollard;"
    echo "  > [-t] for testing the code;"
    echo "  > [-u] for updating the python package."
    exit 1
    ;;
esac
