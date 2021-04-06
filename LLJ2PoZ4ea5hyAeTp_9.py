
import math
def DECIMATOR(txt):
    rm = math.ceil(len(txt)/10)
    txt = txt[0:-rm]
    return txt

