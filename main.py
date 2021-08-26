""" Main exterior file """
import os
import sys

from replace_dollar import main

if __name__ == "__main__":
    main(f"{os.getcwd()}/", sys.argv[1:])
