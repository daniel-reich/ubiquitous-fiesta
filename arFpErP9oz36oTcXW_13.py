
def secret(txt):
    lst = txt.split(".")
    return "<{0} class='{1}'></{0}>".format(lst[0], " ".join(lst[1:]))

