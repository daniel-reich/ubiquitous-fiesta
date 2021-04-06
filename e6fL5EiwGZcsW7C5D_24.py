
def alph_num(txt):
  x = txt.lower()
  new_list = []
  for i in x:
    new_list.append(str(ord(i) - 97))
  return " ".join(new_list)

