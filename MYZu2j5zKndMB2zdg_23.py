
def absolute(txt):
    splitter = txt.split()
    for i in range(len(splitter)):
        if splitter[i]=='a':
            splitter[i]="an absolute"
        elif splitter[i]=='A':
            splitter[i]="An absolute"
    return " ".join(splitter)

