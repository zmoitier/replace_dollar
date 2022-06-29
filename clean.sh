#!/bin/bash

remove_dir() {
    for DIRNAME in $(find . -type d -name $1); do
        rm -dr $DIRNAME
        echo "remove directory: $DIRNAME"
    done
}

remove_file() {
    if [ -f "$1" ]; then
        rm $1
        echo "remove file: $1"
    fi
}

remove_ext() {
    for FILENAME in $(find . -type f -name "*$1"); do
        rm $FILENAME
        echo "remove file: $FILENAME"
    done
}

remove_dir "__pycache__"
remove_dir ".mypy_cache"
remove_dir ".pytest_cache"
remove_dir "htmlcov"

remove_file ".coverage"

for EXT in '.aux' '.bak' '.fdb_latexmk' '.fls' '.log' '.out' '.synctex.gz' '.toc'; do
    remove_ext $EXT
done
