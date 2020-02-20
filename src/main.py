"""
the main program
"""
#!venv/bin/python
import sys
import os
import argparse
import configparser

from reader import Reader
from writer import Writer


DEBUG = True

#FILENAME = "My Clippings.txt"
#DATA_FOLDER = "Data/"
#TAGGED = "Data/Tagged/"
CONFIG_FILE = ".config"


def main():
    """ the main function"""

    if not os.path.exists(CONFIG_FILE):
        print("Error, config file not found!")
        return

    config = configparser.ConfigParser()
    config.read('conf')

    tags = config.get('TAGS', 'tags')
    filename = config.get('FILE', 'filename')
    tagged = config.get('FILE', 'tagged')
    data_folder = config.get('FILE', 'data_folder')


    parser = argparse.ArgumentParser()
    parser.add_argument('kindle', help='path to kindle')
    parser.add_argument('-a', '--auto', help='Automatic mode', action='store_true')
    parser.add_argument('-m', '--manual', help='Manual mode', action='store_true')
    args = parser.parse_args()
    

    reader = Reader(filename)
    writer = Writer(tags, data_folder, tagged)    
    clippings = reader.read()
    if args.manual:
        writer.manual(clippings)
    elif args.auto:
        writer.auto(clippings)
    else:
        writer.auto(clippings)


#def default_config():
#    with open(CONFIG_FILE, "w") as file:
#        file.write("anki\nquote\nnote\n")
#    file.close()

main()
