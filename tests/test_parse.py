"""Test parse."""

from pathlib import Path

import pytest

from replace_dollar.parse_args import parse_args

DIRECTORY = Path.cwd().joinpath("tests", "files")

data_pretty = [(["."], False), (["-s", "."], True)]


@pytest.mark.parametrize("data,result", data_pretty)
def test_pretty(data, result):
    """Test parsing the space flag."""
    _, pretty = parse_args(DIRECTORY, data)
    assert pretty == result


def test_empty_dir():
    """Test empty directory."""
    with pytest.raises(FileNotFoundError):
        parse_args(Path.cwd().joinpath("tests"), ["."])


def test_file_not_found():
    """Test file not found."""
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
    """Test parsing."""
    filenames = set(filepath.name for filepath in parse_args(DIRECTORY, data)[0])
    assert filenames == result
