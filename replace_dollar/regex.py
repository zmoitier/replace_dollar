""" Use regex to do substitution """

import re

DOUBLE_DOLLAR = r"\$\$(.+?)\$\$"

SIMPLE_DOLLAR = r"\$(.+?)\$"

SUB_DOLLAR = [
    (re.compile(DOUBLE_DOLLAR, flags=re.DOTALL), r"\[\1\]"),
    (re.compile(SIMPLE_DOLLAR, flags=re.DOTALL), r"\\(\1\\)"),
]

SUB_PRETTY = [
    (re.compile(r"^([^%\n]*\\\[)\s*(\S)", flags=re.MULTILINE), r"\1\n    \2"),
    (re.compile(r"^([^%\n]*[^%\s])\s*(\\\])", flags=re.MULTILINE), r"\1\n\2"),
    (re.compile(r"(\\\()\s*(\S)"), r"\1 \2"),
    (re.compile(r"(\S)\s*(\\\))"), r"\1 \2"),
]


def do_substitution(content: str, pattern_sub: list[tuple[re.Pattern, str]]) -> str:
    """Do the substitution using pattern and sub."""

    for pattern, sub in pattern_sub:
        content = pattern.sub(sub, content)

    return content
