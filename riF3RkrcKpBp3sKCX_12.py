
def cap_space(txt):
  return "".join(" " + i.lower() if i.isupper()==True else i for i in txt)

