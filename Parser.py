FILENAME = "My Clippings.txt"

def parse():
    with open("Kindle_Clippings_Parser/"+FILENAME) as file:
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
            handle_clipping(clipping)
            print("next")


def handle_clipping(clipping):
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
    
    with open(Title + "_" + tag, "a") as file:
        file.write(Text + "\n") 
    file.close()

            

# def manage_clipping(clipping):
#     Title = clipping[0]
#     Metadata = clipping[1].split("|")
#     Page = Metadata[0]
#     Date = Metadata[1]
#     Text = clipping[3]
#     print("Title: " + Title)
#     print("Page Number: " + Page)
#     print("Date: " + Date)
#     print("Text: " + Text)


parse()