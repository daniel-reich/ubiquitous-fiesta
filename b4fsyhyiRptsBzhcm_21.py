
def sum_even_nums_in_range(start, stop):
  new = []
  for i in range(start, stop+1):
    if i % 2 == 0:
      new.append(i)
  return sum(new)

