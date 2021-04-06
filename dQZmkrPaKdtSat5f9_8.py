
def single_occurrence(txt):
    txt = txt.upper()
    return ''.join(filter(lambda i: txt.count(i)==1, txt))

