
def first_non_repeated_character(txt):
  txt = [i for i in txt if txt.count(i)==1]
  if len(txt)==0:
    return False
  else:
    return txt[0]

