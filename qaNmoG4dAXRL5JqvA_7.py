
def sum_fractions(lst):
  print(lst)
  s1 = 0
  for i in range(len(lst)):
    s1 += (lst[i][0]/lst[i][1])
  return round(s1)

