#!/bin/python
import Parser
import sys


def main():
    if len(sys.argv) == 3:
        mode = sys.argv[2]

    option = sys.argv[1]

    if option in ["-h", "--help"]:
        helper()

    if option in ["-p", "--parse"]:
        Parser.parse(mode)

def helper():
    print(
        "\nUsage: ./Main.py [OPTIONS] [ARGUMENTS]...\n\n\
            A simple script to manage Kindle clippings\n\n\
            Options:\n\
            \t -h, --help\tPrint this help\n\
            \t -p, --parse\tRead Clippings.txt file\n"
            )

main()
