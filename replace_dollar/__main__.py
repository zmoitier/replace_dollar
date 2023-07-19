"""Main file."""

import sys
from pathlib import Path
from shutil import copyfile

from .parse_args import parse_args
from .regex import do_substitution


def make_bakup(filepath: Path) -> None:
    """Make a bakup of the file."""
    copyfile(filepath, filepath.parent.joinpath(f"{filepath.stem}.bak"))


def process_file(filepath: Path, pretty: bool) -> None:
    """Process the file."""

    print(f"Processing file ´{filepath.name}´")

    make_bakup(filepath)
    print(f"  > bakup file ´{filepath.stem}.bak´ created")

    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()

    content = do_substitution(content, pretty)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)

    print("  > substitution done!", end="\n\n")


def main(directory: Path, argv: list[str]) -> None:
    """Main function."""

    filepaths, space = parse_args(directory, argv)

    for filepath in filepaths:
        process_file(filepath, space)


if __name__ == "__main__":
    main(Path.cwd(), sys.argv[1:])
