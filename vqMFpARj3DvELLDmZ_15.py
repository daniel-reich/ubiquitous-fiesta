
def letters_only(txt):
  a = [x for x in txt if x.isalpha()]
  return "".join(a)

