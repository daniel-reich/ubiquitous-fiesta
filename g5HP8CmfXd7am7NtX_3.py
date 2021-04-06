
def keyboard_mistakes(txt):
     a = txt.maketrans("4501","ASOI")
     return txt.translate(a)

