
def dial(txt):
    d = "abc def ghi jkl mno pqrstuv wxyz"
    return "".join(str(d.index(c)//4+2) if c.isalpha() else c for c in txt.lower())

