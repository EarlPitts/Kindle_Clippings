"""
module for reading in from clippings file
"""

#!env/bin/python

class Reader:
    """ the class that provides the reading functionalities """

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        """ the maint function to read from file """
        with open(self.filename) as file:
            data = file.readlines()

            clippings = []
            clipping = []

            for line in data:
                if line == "==========\n":
                    clippings.append(tuple(clipping.copy()))
                    clipping.clear()
                else:
                    clipping.append(line)
        file.close()
        return clippings
