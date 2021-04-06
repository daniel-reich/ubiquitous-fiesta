
def name_shuffle(txt):
  a = txt.split(" ")
  a[0],a[1] = a[1],a[0]
  return " ".join(a)

