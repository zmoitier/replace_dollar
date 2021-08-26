""" Replace dollar

    Author: Zoïs Moitier
            Karlsruhe Institute of Technology, Germany

    Description
    -----------
    Replace the Tex commands $...$ and $$...$$ by the LaTeX
    commands \\(...\\) and \\[...\\] in `.tex` files.
"""

__version__ = "1.0.0"

from .__main__ import main
