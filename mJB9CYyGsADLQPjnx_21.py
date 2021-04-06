
def first_non_repeated_character(txt):
    b=[i for i in txt if txt.count(i)==1]
    if len(b)>=1:
        return b[0]
    else:
        return False

