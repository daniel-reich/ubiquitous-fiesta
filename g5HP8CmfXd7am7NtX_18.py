
def keyboard_mistakes(txt):
    a = {"0":"O", "1":"I", "4":"A", "5":"S"}
    return "".join(a[i] if i in a else i for i in txt)

