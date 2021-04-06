
def all_about_strings(txt):
  return [
    len(txt),
    txt[0],
    txt[-1],
    txt[(len(txt)-1)//2:(len(txt)+2)//2],
    "@ index {}".format(txt.index(txt[1], 2)) if txt[1] in txt[2:] else "not found"
  ]

