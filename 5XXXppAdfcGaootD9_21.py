
def sum_odd_and_even(lst):
  lst1 = [0, 0]
  t1 = 0
  t2 = 0
  for i in lst:
    if (i % 2) == 0:
      t1+=i
    else:
      t2+=i
  lst1 = [t1, t2]
  print(lst1)
  return lst1

