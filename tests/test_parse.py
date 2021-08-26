""" Test parse """
import os

import pytest

from replace_dollar.parse_args import parse_args

DIR = f"{os.getcwd()}/tests/"


def test_pretty():
    _, p = parse_args(DIR, ["-p", "."])
    assert p


data_file = [
    (["."], {"file.tex"}),
    (["file.tex"], {"file.tex"}),
    (["file1.tex", "file2.tex"], {"file1.tex", "file2.tex"}),
    (["file1.tex", "file2.txt", "file3.tex"], {"file1.tex", "file3.tex"}),
]


@pytest.mark.parametrize("data,result", data_file)
def test_file(data, result):
    filenames, _ = parse_args(DIR, data)
    assert filenames == result
