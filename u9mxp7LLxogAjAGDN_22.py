
def factor_sort(lst):
  factors = []
  for x in range(0, len(lst)):
    num = lst[x]
    count = 0
    for x in range(1, num+1):
      for y in range(1, num+1):
        if x*y == num:
          count += 1
    factors.append(count)
  zipped_pairs = zip(factors, lst) 
  z = [x for _, x in sorted(zipped_pairs, reverse = True)] 
  return(z)

