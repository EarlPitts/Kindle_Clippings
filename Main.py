#!env/bin/python
from Parser import Parser
import sys
import os


FILENAME = "My Clippings.txt"
DATA_FOLDER = "Data/"
TAGGED = "Data/Tagged/"
CONFIG_FILE = ".config"

def main():

    tags = []


    if not os.path.exists(CONFIG_FILE):
        print("Error, config file not found!") 

    with open(CONFIG_FILE, "r") as file:
        for line in file:
            tags.append(line)
    file.close()

    if len(sys.argv) == 3:
        mode = sys.argv[2]

    option = sys.argv[1]


    if option in ["-h", "--help"]:
        helper()

    if option in ["-p", "--parse"]:
        parser = Parser(FILENAME, DATA_FOLDER, TAGGED, tags)
        if mode == "-i":
            parser.manual()

        if mode == "-a":
            parser.auto()

def helper():
    print(
        "\nUsage: ./Main.py [OPTIONS] [ARGUMENTS]...\n\n\
            A simple script to manage Kindle clippings\n\n\
            Options:\n\
            \t -h, --help\tPrint this help\n\
            \t -p, --parse\tRead Clippings.txt file\n"
            )

#def default_config():
#    with open(CONFIG_FILE, "w") as file:
#        file.write("anki\nquote\nnote\n")
#    file.close()

main()
