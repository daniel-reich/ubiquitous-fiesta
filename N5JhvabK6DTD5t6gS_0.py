
def markdown(symb):
    def change(txt, mark):
        return ' '.join(symb+i+symb if mark.lower() in i.lower() else i for i in txt.split())
    return change

