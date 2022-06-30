""" Test substitution on string """

import pytest

from replace_dollar.regex import do_substitution

data_regex = [
    ("$x$", "\\(x\\)"),
    ("$\n    x\n$", "\\(\n    x\n\\)"),
    ("\\(x\\)", "\\(x\\)"),
    ("$$x$$", "\\[x\\]"),
    ("$$\n    x\n$$", "\\[\n    x\n\\]"),
    ("\\[x\\]", "\\[x\\]"),
]


@pytest.mark.parametrize("data,result", data_regex)
def test_regex(data, result):
    """Test regex."""
    assert do_substitution(data, False) == result


data_regex_space = [
    ("$x$", "\\( x \\)"),
    ("$\n    x\n$", "\\(\n    x\n\\)"),
    ("\\(x\\)", "\\( x \\)"),
    ("$$x$$", "\\[ x \\]"),
    ("$$\n    x\n$$", "\\[\n    x\n\\]"),
    ("\\[x\\]", "\\[ x \\]"),
]


@pytest.mark.parametrize("data,result", data_regex_space)
def test_regex_space(data, result):
    """Test regex with space."""
    assert do_substitution(data, True) == result
