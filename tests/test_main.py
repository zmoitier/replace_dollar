""" Test __main__ """
import filecmp
import os
from shutil import copyfile

from replace_dollar.__main__ import main, make_bakup

DIR = f"{os.getcwd()}/tests/"


def test_make_clean():
    make_bakup(DIR, "file.tex")
    assert filecmp.cmp(f"{DIR}file.tex", f"{DIR}file.tex.bak")


def test_main():
    copyfile(f"{DIR}files/file.tex", f"{DIR}file.tex")
    main(DIR, ["file.tex"])
    assert filecmp.cmp(f"{DIR}file.tex", f"{DIR}files/reference.tex")


def test_main_pretty():
    copyfile(f"{DIR}files/file.tex", f"{DIR}file.tex")
    main(DIR, ["-p", "file.tex"])
    assert filecmp.cmp(f"{DIR}file.tex", f"{DIR}files/reference_pretty.tex")
