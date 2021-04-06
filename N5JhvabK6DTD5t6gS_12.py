
def markdown(symb):
    return lambda x,y: " ".join(((symb+i+symb) if i.lower().strip("!?.") == y.lower() else i for i in x.split(" ")))

