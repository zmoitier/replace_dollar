""" Main file """

import re
import sys
from pathlib import Path
from shutil import copyfile

from .parse_args import parse_args
from .regex import SUB_DOLLAR, SUB_PRETTY, do_substitution


def make_bakup(filepath: Path) -> None:
    """Make a bakup of the file."""
    copyfile(filepath, filepath.parent.joinpath(f"{filepath.stem}.bak"))
    return None


def process_file(filepath: Path, pattern_sub: list[tuple[re.Pattern, str]]) -> None:
    """Process the file"""

    print(f"Processing file `{filepath.name}`")

    make_bakup(filepath)
    print(f"  > bakup file `{filepath.stem}.bak` created")

    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()

    content = do_substitution(content, pattern_sub)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)

    print("  > substitution done!", end="\n\n")

    return None


def main(directory: Path, argv: list[str]) -> None:
    """Main function"""

    filepaths, pretty = parse_args(directory, argv)

    if not filepaths:
        sys.exit(f"No files found in {directory}")

    if pretty:
        pattern_sub = [*SUB_DOLLAR, *SUB_PRETTY]
    else:
        pattern_sub = SUB_DOLLAR

    for filepath in filepaths:
        process_file(filepath, pattern_sub)

    return None


if __name__ == "__main__":
    main(Path.cwd(), sys.argv[1:])
