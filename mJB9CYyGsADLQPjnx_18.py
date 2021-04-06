
def first_non_repeated_character(txt):
  l=[i for i in txt if txt.count(i)==1]
  return l[0] if len(l)>0 else False

