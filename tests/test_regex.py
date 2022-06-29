""" Test substitution on string """

import pytest

from replace_dollar.regex import do_substitution

data_regex = [
    ("$x$", "\\(x\\)"),
    ("\\(x\\)", "\\(x\\)"),
    ("$$x$$", "\\[x\\]"),
    ("\\[x\\]", "\\[x\\]"),
]


@pytest.mark.parametrize("data,result", data_regex)
def test_regex(data, result):
    """test regex"""
    assert do_substitution(data, False) == result
