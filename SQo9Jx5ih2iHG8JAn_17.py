
def expanded_form(num):
    s = str(num)
    len_s = len(s)
    return " + ".join("{}{}".format(c, "0" * (len_s - 1 - i))
                      for i, c in enumerate(s) if c != "0")

