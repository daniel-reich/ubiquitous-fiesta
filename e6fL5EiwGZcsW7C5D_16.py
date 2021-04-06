
import string
def alph_num(txt):
    abc_ = string.ascii_uppercase
    return " ".join([str(abc_.index(i)) for i in txt])

