
def direction(lst):
  nlst = []
  for item in lst:
    nlst.append(item.replace("e", "w").replace("E", "W").replace("a", "e").replace("A", "E"))
  return nlst

