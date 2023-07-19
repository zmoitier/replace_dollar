"""Use regex to do substitution.

The regular expressions used here are heavily inspire by the one in the
post
https://stackoverflow.com/questions/14182879/regex-to-match-latex-equations.
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

SPACE_LINE = r"""
(?<!\\)(\\\(|\\\[)
(?:[^\S\n]*)
(\S.*?)
(?:[^\S\n]*)
(?<!\\)(\\\)|\\\])
"""

ADD_SPACE = [(re.compile(SPACE_LINE, flags=re.DOTALL | re.VERBOSE), r"\1 \2 \3")]


def do_substitution(content: str, space: bool) -> str:
    """Do the substitution using pattern and sub."""

    for pattern, sub in SUB_DOLLAR:
        content = pattern.sub(sub, content)

    if space:
        for pattern, sub in ADD_SPACE:
            content = pattern.sub(sub, content)

    return content
