
def best_friend(txt, a, b):
  res = [i for i in txt.split() if a in i]
  try:
    return all([i.index(a) + 1 == i.index(b) and i.rindex(a) == i.index(a) for i in res])
  except:
    return False

