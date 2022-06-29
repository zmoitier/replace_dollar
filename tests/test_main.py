""" Test __main__ """

import filecmp
from pathlib import Path
from shutil import copyfile

from replace_dollar.__main__ import main, make_bakup

DIRECTORY = Path.cwd().joinpath("tests", "files")


def test_make_clean():
    """test clean"""
    make_bakup(DIRECTORY.joinpath("main.tex"))
    assert filecmp.cmp(DIRECTORY.joinpath("main.tex"), DIRECTORY.joinpath("main.bak"))


def test_main():
    """main"""
    copyfile(DIRECTORY.joinpath("main_tex.tex"), DIRECTORY.joinpath("main.tex"))
    main(DIRECTORY, ["main.tex"])
    assert filecmp.cmp(
        DIRECTORY.joinpath("main.tex"), DIRECTORY.joinpath("main_latex.tex")
    )
