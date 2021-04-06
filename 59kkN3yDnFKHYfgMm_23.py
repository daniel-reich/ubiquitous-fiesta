
def best_friend(txt, a, b):
  if a==b:
    return False
  else:
    arr=[x for x in txt.split(" ") if a in x]
    return sum([list(x) for x in arr],[]).count(a) <= sum([list(y) for y in arr],[]).count(b)

