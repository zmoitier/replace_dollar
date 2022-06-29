""" Test substitution on string """

import pytest

from replace_dollar.regex import SUB_DOLLAR, SUB_PRETTY, do_substitution

data_simple_dollar = [
    ("$x$", "\\(x\\)"),
    ("$x$ and $y$", "\\(x\\) and \\(y\\)"),
    ("$\nx\n$", "\\(\nx\n\\)"),
]


@pytest.mark.parametrize("data,result", data_simple_dollar)
def test_simple_dollar(data, result):
    assert do_substitution(data, SUB_DOLLAR) == result


data_double_dollar = [
    ("$$x$$", "\\[x\\]"),
    ("$$\nx\n$$", "\\[\nx\n\\]"),
]


@pytest.mark.parametrize("data,result", data_double_dollar)
def test_double_dollar(data, result):
    assert do_substitution(data, SUB_DOLLAR) == result


data_mix_dollar = [
    ("$$\text{$x$ and $y$}$$", "\\[\text{\\(x\\) and \\(y\\)}\\]"),
]


@pytest.mark.parametrize("data,result", data_mix_dollar)
def test_mix_dollar(data, result):
    assert do_substitution(data, SUB_DOLLAR) == result


data_simple_pretty = [
    ("\\(x\\)", "\\( x \\)"),
    ("\\( x \\)", "\\( x \\)"),
    ("\\(\nx\n\\)", "\\( x \\)"),
]


@pytest.mark.parametrize("data,result", data_simple_pretty)
def test_simple_pretty(data, result):
    assert do_substitution(data, SUB_PRETTY) == result


data_double_pretty = [
    ("\\[x\\]", "\\[\n    x\n\\]"),
    ("\\[ x \\]", "\\[\n    x\n\\]"),
    ("\\[\n    x\n\\]", "\\[\n    x\n\\]"),
]


@pytest.mark.parametrize("data,result", data_double_pretty)
def test_double_pretty(data, result):
    assert do_substitution(data, SUB_PRETTY) == result
