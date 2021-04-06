
def wumbo(words):
    new = ""
    for i in words:
        if i == "M":
            i = "W"
        new = new+i
    return new

