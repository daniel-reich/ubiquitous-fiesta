
def blah_blah(txt, n):
    return " ".join(txt.split()[:-n])+" "+"blah "*(n-1)+"blah..." if n<len(txt.split()) else "blah "*(len(txt.split())-1)+"blah..."

