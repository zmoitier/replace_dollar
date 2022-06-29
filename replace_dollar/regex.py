""" Use regex to do substitution

    The regular expressions used here are heavily inspire by the one in the post
    https://stackoverflow.com/questions/14182879/regex-to-match-latex-equations.
    https://stackoverflow.com/questions/2973436/regex-lookahead-lookbehind-and-atomic-groups
"""

import re

SIMPLE_DOLLAR = r"""
(?<!\\)
(?:
    ((?<!\$)\${1}(?!\$))
)
(.*?)
(?<!\\)
(?<!\$)\1(?!\$)
"""

DOUBLE_DOLLAR = r"""
(?<!\\)
(?:
    ((?<!\$)\${2}(?!\$))
)
(.*?)
(?<!\\)
(?<!\$)\1(?!\$)
"""

SUB_DOLLAR = [
    (re.compile(DOUBLE_DOLLAR, flags=re.MULTILINE | re.DOTALL | re.VERBOSE), r"\[\2\]"),
    (re.compile(SIMPLE_DOLLAR, flags=re.MULTILINE | re.DOTALL | re.VERBOSE), r"\(\2\)"),
]

SUB_PRETTY = [
    (re.compile(r"^([^%\n]*\\\[)\s*(\S)", flags=re.MULTILINE), r"\1\n    \2"),
    (re.compile(r"^([^%\n]*[^%\s])\s*(\\\])", flags=re.MULTILINE), r"\1\n\2"),
    (re.compile(r"(\\\()\s*(\S)"), r"\1 \2"),
    (re.compile(r"(\S)\s*(\\\))"), r"\1 \2"),
]


def do_substitution(content: str, pretty: bool) -> str:
    """Do the substitution using pattern and sub."""

    for pattern, sub in SUB_DOLLAR:
        content = pattern.sub(sub, content)

    if pretty:
        for pattern, sub in SUB_PRETTY:
            content = pattern.sub(sub, content)

    return content
