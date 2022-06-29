""" Test parse """

from pathlib import Path

import pytest

from replace_dollar.parse_args import parse_args

DIRECTORY = Path.cwd().joinpath("tests", "files")


def test_not_file():
    """test parsing"""
    with pytest.raises(FileNotFoundError):
        parse_args(DIRECTORY, ["file.tex"])


data_file = [
    (["main.tex"], {"main.tex"}),
    (["main.txt"], set()),
    (["main.tex", "main_tex.tex"], {"main.tex", "main_tex.tex"}),
    (["main.tex", "main.txt"], {"main.tex"}),
    (["."], {"main.tex", "main_tex.tex", "main_latex.tex"}),
]


@pytest.mark.parametrize("data,result", data_file)
def test_file(data, result):
    """test parsing"""
    filenames = set(filepath.name for filepath in parse_args(DIRECTORY, data)[0])
    assert filenames == result
