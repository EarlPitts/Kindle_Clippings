import os

class Writer:

    def __init__(self, tags, data_folder, tagged):
        self.data_folder = data_folder
        self.tags = tags
        self.tagged = tagged


    def manual(self, clippings):
        d = {clipping:"x" for clipping in clippings}

        d_keys = list(d.keys())

        i = 0
        while i < len(d_keys):
            Title = d_keys[i][0]
            Metadata = d_keys[i][1].split("|")
            Page = d_keys[i][0]
            Date = d_keys[i][1]
            Text = d_keys[i][3]
            print("Title: " + Title)
            print("Page Number: " + Page)
            print("Date: " + Date)
            print("Text: " + Text)

            print("Tags: ", end="")
            for tag in self.tags:
                print(tag + ", ", end="")
            print("\n")
                    
            d_tag = input("Enter tag: ")

            if d_tag == "n":
                i += 1

            elif d_tag == "p":
                i -= 1     
            
            else:
                d[d_keys[i]] = d_tag
                i += 1

        for clipping, d_tag in d.items():
            if d_tag != "x":

                if not os.path.exists(self.tagged + d_tag):
                    os.makedirs(self.tagged + d_tag)

                with open(self.tagged + d_tag + "/" + clipping[0], "a") as file:
                    file.write(clipping[3] + "\n") 
                file.close()

    def auto(self, clippings):
        for clipping in clippings:
            Title = clipping[0]
            Text = clipping[3]

            if not os.path.exists(self.data_folder):
                os.makedirs(self.data_folder)

            with open(self.data_folder + str(Title).rstrip() + '.md', "a") as file:
                file.write(Text + "\n")
            file.close()