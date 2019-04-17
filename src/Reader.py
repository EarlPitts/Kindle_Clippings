#!env/bin/python

class Reader:

    def __init__(self, filename):
        self.filename = filename

    def read(self):
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


