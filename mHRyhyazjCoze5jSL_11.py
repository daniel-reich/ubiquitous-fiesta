
def double_swap(txt, c1, c2):
    return txt.translate(txt.maketrans(c1 + c2,c2 + c1))

