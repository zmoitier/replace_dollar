""" Parse arguments given in the command line """
import argparse
import os
from typing import Tuple

DESCRIPTION = (
    "Replace the Tex commands $...$ and $$...$$ by the LaTeX "
    "commands \\(...\\) and \\[...\\] in `.tex` files."
)


def parse_args(dir: str, argv: list[str]) -> Tuple[set[str], bool]:
    """parse arguments given in the command line"""

    parser = argparse.ArgumentParser(
        description=DESCRIPTION, formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "filename",
        help=(
            "the list of `.tex` files or\n"
            f"`.` for all the `.tex` files in the directory {dir}"
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
        action="store_true",
    )

    args = parser.parse_args(args=argv if argv else ["--help"])

    if "." in args.filename:
        list_search = os.listdir(dir)
    else:
        list_search = args.filename

    return (set(filter(lambda s: s.endswith(".tex"), list_search)), args.pretty)
