
def is_central(txt):
  i = [i for i in txt if i != " "][0]
  j = txt.split(i)
  return j[0] == j[1]

