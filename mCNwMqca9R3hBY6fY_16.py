
def make_happy(txt):
  return "".join([")" if v == "(" and (txt[i-1] == "8" or txt[i-1] == ":" or txt[i-1] == ";" or txt[i-1] == "x") else v for i,v in enumerate(txt)])

