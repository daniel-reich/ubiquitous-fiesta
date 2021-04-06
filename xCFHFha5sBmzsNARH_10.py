
def reverse(txt):
    if txt == "":
        return txt
    else:
        return reverse(txt[1:]) + txt[0]

