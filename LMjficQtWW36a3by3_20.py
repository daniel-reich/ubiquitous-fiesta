
def probability(lst, n):
  x=0
  for number in lst:
    if number >= n:
      x+=1
  return round(x / len(lst) * 100, 1)

