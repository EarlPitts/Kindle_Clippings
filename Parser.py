#!env/bin/python
import os
import keyboard

class Parser:

    def __init__(self, filename, data_folder, tagged, tags):
        self.filename = filename
        self.data_folder = data_folder
        self.tagged = tagged
        self.tags = tags
        self.clippings = []
        self.parse()



    def parse(self):
        with open(self.filename) as file:
            data = file.readlines()

            self.clippings = []
            clipping = []

            for line in data:
                if line == "==========\n":
                    self.clippings.append(clipping.copy())
                    clipping.clear()
                else:
                    clipping.append(line)



    def manual(self):
        for clipping in self.clippings:
            Title = clipping[0]
            Metadata = clipping[1].split("|")
            Page = Metadata[0]
            Date = Metadata[1]
            Text = clipping[3]
            print("Title: " + Title)
            print("Page Number: " + Page)
            print("Date: " + Date)
            print("Text: " + Text)

            print("Tags:\n")
            for tag in self.tags:
                print(tag + "\n")

            while True:
                try:
                    if keyboard.is_pressed("a"):
                        tag = "anki"
                        break
                    if keyboard.is_pressed("n"):
                        tag = "notes"
                        break
                    if keyboard.is_pressed("q"):
                        tag = "quote"
                        break
                    else:
                        pass
                except:
                    break

            #tag = input("Add tag: ")
            #if tag == "x":
            #    return

            if not os.path.exists(self.tagged + tag):
                os.makedirs(self.tagged + tag)

            with open(self.tagged + tag + "/" + Title, "a") as file:
                file.write(Text + "\n") 
            file.close()


    def auto(self):
        for clipping in self.clippings:
            Title = clipping[0]
            Text = clipping[3]

            if not os.path.exists(self.data_folder):
                os.makedirs(self.data_folder)

            with open(self.data_folder + Title, "a") as file:
                file.write(Text + "\n")
            file.close()