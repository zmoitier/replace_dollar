""" Main file """

import os
import re
import sys
from shutil import copyfile
from typing import Tuple

from .parse_args import parse_args
from .regex import SUB_DOLLAR, SUB_PRETTY, do_substitution


def make_bakup(directory: str, filename: str) -> None:
    """Make a bakup of the file."""
    copyfile(f"{directory}{filename}", f"{directory}{filename}.bak")
    return None


def process_file(
    directory: str, filename: str, pattern_sub: list[Tuple[re.Pattern, str]]
) -> None:
    """Process the file"""

    print(f"Processing file `{filename}`")

    make_bakup(directory, filename)
    print(f"  > bakup file `{filename}.bak` created")

    with open(f"{directory}{filename}", "r") as file:
        content = file.read()

    content = do_substitution(content, pattern_sub)

    with open(f"{directory}{filename}", "w") as file:
        file.write(content)

    print(f"  > substitution done!", end="\n\n")

    return None


def main(directory: str, argv: list[str]) -> None:
    """Main function"""

    filenames, pretty = parse_args(directory, argv)

    if not filenames:
        sys.exit(f"No files found in {directory}")

    if pretty:
        pattern_sub = [*SUB_DOLLAR, *SUB_PRETTY]
    else:
        pattern_sub = SUB_DOLLAR

    for filename in filenames:
        process_file(directory, filename, pattern_sub)

    return None


if __name__ == "__main__":
    main(f"{os.getcwd()}/", sys.argv[1:])
