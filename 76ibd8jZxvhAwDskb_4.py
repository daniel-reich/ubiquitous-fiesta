
def tallest_skyscraper(lst):
  s, lst2 = 0, []
  for i in range (len(lst[0])):
    for j in range(len(lst)):
      s += lst[j][i]
    lst2.append(s)
    s = 0
  return max(lst2)

