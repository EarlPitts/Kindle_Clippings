FILENAME = "My Clippings.txt"

def parse():
    with open(FILENAME) as file:
        data = file.readlines()

        clippings = []
        clipping = []

        for line in data:
            if line == "==========\n":
                clippings.append(clipping)
                clipping.clear()
            else:
                clipping.append(line)

        for clipping in clippings:
            manage_clipping(clipping)

            

def manage_clipping(clipping):
    Title = clipping[0]
    Metadata = clipping[1].split("|")
    Page = Metadata[0]
    Date = Metadata[1]
    Text = clipping[3]
    print("Title: " + Title)
    print("Page Number: " + Page)
    print("Date: " + Date)
    print("Text: " + Text)


parse()