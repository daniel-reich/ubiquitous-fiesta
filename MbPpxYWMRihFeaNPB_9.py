
def sum_of_evens(lst):
  even_sum = 0
  for i in lst:
    for x in i:
      if x % 2 == 0:
        even_sum = even_sum +x
  return even_sum

