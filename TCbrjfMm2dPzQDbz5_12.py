
def insert_whitespace(txt):
    string = txt[0]
    for i in range(1,len(txt)):
        if txt[i].isupper():
            string += ' ' + txt[i]
        else:
            string += txt[i]
    return string

