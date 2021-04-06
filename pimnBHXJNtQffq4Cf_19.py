
def mapping(letters):
  dic = {}
  for i in letters:
    dic.setdefault(i, i.upper())
  return dic

