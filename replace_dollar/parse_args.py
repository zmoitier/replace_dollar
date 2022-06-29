""" Parse arguments given in the command line """

import argparse
from pathlib import Path

DESCRIPTION = (
    "Replace the Tex commands $...$ and $$...$$ by the LaTeX "
    "commands \\( ... \\) and \\[\n    ...\n\\] in `.tex` files."
)


def _check_file_exist(filepaths: set[Path]) -> None:
    """Check if a file exist."""
    for filepath in filepaths:
        print(filepath)
        if not filepath.is_file():
            raise FileNotFoundError(f"the file {filepath} does not exist.")


def parse_args(directory: Path, argv: list[str]) -> tuple[set[Path], bool]:
    """parse arguments given in the command line"""

    parser = argparse.ArgumentParser(
        description=DESCRIPTION, formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "filename",
        help=(
            "the list of `.tex` files or\n"
            f"`.` for all the `.tex` files in the directory {directory}"
        ),
        nargs="+",
    )

    parser.add_argument(
        "-p",
        "--pretty",
        help=(
            "add space to \\( ... \\) and newline to \\[\\n ... \\n\\]\n"
            "do nothing on \\[ ... \\] in commented section"
        ),
        action=argparse.BooleanOptionalAction,
        default=False,
    )

    args = parser.parse_args(args=argv if argv else ["--help"])

    if "." in args.filename:
        set_search = set(directory.glob("*.tex"))
    else:
        set_search = set(
            directory.joinpath(filename)
            for filename in filter(lambda s: s.endswith(".tex"), args.filename)
        )
        _check_file_exist(set_search)

    return (set_search, args.pretty)
