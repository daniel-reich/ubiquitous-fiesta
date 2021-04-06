
def alph_num(txt):
  lst = [str(ord(x)-65) for x in txt]
  return " ".join(lst)

