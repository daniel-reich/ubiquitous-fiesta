
def sum_of_evens(lst):
  sum=0
  for sub in lst:
    for sub_sub in sub:
      if sub_sub%2==0:
        sum+=sub_sub
  return sum

