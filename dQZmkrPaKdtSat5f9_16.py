
def single_occurrence(txt):
    txt = txt.upper()
    lst = []
    for char in txt:
        lst.append((char, txt.count(char)))
    for i in lst:
        if i[1] == 1:
          return i[0]
    return ""

