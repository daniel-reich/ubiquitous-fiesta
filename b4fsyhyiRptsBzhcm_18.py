
def sum_even_nums_in_range(start, stop):
  x = range(start, stop+1)
  sumnum = []
  for y in x:
    if y%2 == 0:
      sumnum.append(y)
  return sum(sumnum)

