
def simon_says(lst1, lst2):
  return not any(x - y for x, y in zip(lst1, lst2[1:]))

