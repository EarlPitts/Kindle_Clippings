import os

class Writer:

    def __init__(self, tags, data_folder):
        self.data_folder = data_folder
        self.tags = tags


    def manual(self, clippings):
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

            #while True:
            #    try:
            #        if keyboard.is_pressed("a"):
            #            tag = "anki"
            #            break
            #        if keyboard.is_pressed("n"):
            #            tag = "notes"
            #            break
            #        if keyboard.is_pressed("q"):
            #            tag = "quote"
            #            break
            #        else:
            #            pass
            #    except:
            #        break

            #tag = input("Add tag: ")
            #if tag == "x":
            #    return

            if not os.path.exists(self.tagged + tag):
                os.makedirs(self.tagged + tag)

            with open(self.tagged + tag + "/" + Title, "a") as file:
                file.write(Text + "\n") 
            file.close()


    def auto(self, clippings):
        for clipping in clippings:
            Title = clipping[0]
            Text = clipping[3]

            if not os.path.exists(self.data_folder):
                os.makedirs(self.data_folder)

            with open(self.data_folder + Title, "a") as file:
                file.write(Text + "\n")
            file.close()