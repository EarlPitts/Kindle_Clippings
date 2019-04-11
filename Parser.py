#!/bin/python
import os

FILENAME = "My Clippings.txt"
DATA_FOLDER = "Data/"
TAGGED = "Data/Tagged/"

def parse(mode):

    with open(FILENAME) as file:
        data = file.readlines()

        clippings = []
        clipping = []

        for line in data:
            if line == "==========\n":
                clippings.append(clipping.copy())
                clipping.clear()
            else:
                clipping.append(line)

        for clipping in clippings:
            if mode == "-i":
                manual(clipping)
            if mode == "-a":
                auto(clipping)


def manual(clipping):
    Title = clipping[0]
    Metadata = clipping[1].split("|")
    Page = Metadata[0]
    Date = Metadata[1]
    Text = clipping[3]
    print("Title: " + Title)
    print("Page Number: " + Page)
    print("Date: " + Date)
    print("Text: " + Text)

    tag = input("Add tag: ")
    if tag == "x":
        return

    if not os.path.exists(TAGGED + tag):
        os.makedirs(TAGGED + tag)
    
    with open(TAGGED + tag + "/" + Title, "a") as file:
        file.write(Text + "\n") 
    file.close()


def auto(clipping):
    Title = clipping[0]
    Text = clipping[3]

    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    with open(DATA_FOLDER + Title, "a") as file:
        file.write(Text + "\n")
    file.close()