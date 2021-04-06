
def expanded_form(num):
    whole, fraction = str(num).split(".")
    len_w, lst = len(whole), []
    for i, c in enumerate(whole):
        if c != "0":
            lst.append("{}{}".format(c, "0" * (len_w - 1 - i)))
    for i, c in enumerate(fraction):
        if c != "0":
            lst.append("{}/1{}".format(c, "0" * (i + 1)))
    return " + ".join(lst)

