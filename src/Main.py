#!env/bin/python
from Reader import Reader 
from Writer import Writer

import sys
import os

#FILENAME = "My Clippings.txt"
#DATA_FOLDER = "Data/"
#TAGGED = "Data/Tagged/"
CONFIG_FILE = ".config"

def main():

    tags = []

    if not os.path.exists(CONFIG_FILE):
        print("Error, config file not found!") 

    with open(CONFIG_FILE, "r") as file:
        for line in file:
            if "#" in line:
                pass
            if "FILENAME" in line:
                FILENAME = line.split("=")[1].strip()
            if "DATA_FOLDER" in line:
                DATA_FOLDER = line.split("=")[1].rstrip()
            if "TAGGED_FOLDER" in line:
                TAGGED = line.split("=")[1].rstrip()
            if "TAGS" in line:
                tags = line.split("=")[1].rstrip().split(",")
    file.close()

    option = sys.argv[1]

    if option in ["-h", "--help"]:
        helper()
    else:
        reader = Reader(FILENAME)
        writer = Writer(tags, DATA_FOLDER, TAGGED)
        clippings = reader.read()
        print(type(clippings))
        if option == "-i":
            writer.manual(clippings)

        if option == "-a":
            writer.auto(clippings)


def helper():
    print(
        "\nUsage: ./Main.py [OPTIONS] [ARGUMENTS]...\n\n\
            A simple script to manage Kindle clippings\n\n\
            Options:\n\
            \t -h, --help\tPrint this help\n\
            \t -a, --auto\tAuto mode\n\
            \t -i, --i\tInteractive mode\n"
            )

#def default_config():
#    with open(CONFIG_FILE, "w") as file:
#        file.write("anki\nquote\nnote\n")
#    file.close()

main()
