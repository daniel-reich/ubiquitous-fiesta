
def even_odd_string(txt):
  e, o = "".join(txt[::2]), "".join(txt[1::2])
  return "{} {}".format(e, o)

