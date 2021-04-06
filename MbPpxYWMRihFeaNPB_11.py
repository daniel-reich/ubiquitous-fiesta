
def sum_of_evens(lst):
  sum=0
  for l in lst:
    for n in l:
      if n%2==0:
        sum+=n
  return sum

