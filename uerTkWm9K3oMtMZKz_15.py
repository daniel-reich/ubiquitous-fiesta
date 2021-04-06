
def sweetest_icecream(lst):
  res = []
  dic = {
    "Plain" : 0,
    "Vanilla" : 5,
    "ChocolateChip" : 5,
    "Strawberry" : 10,
    "Chocolate" : 10,
  }
  for i in lst:
    s = i.num_sprinkles + dic.get(i.flavor)
    res.append(s)
  return max(res)

