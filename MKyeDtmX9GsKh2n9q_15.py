
def gen_deck():
  lst = []
  lst2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
  lst3 = ["d", "c", "h", "s"]
  for i in lst3:
    for j in lst2:
      lst.append((j, i))
  return lst

