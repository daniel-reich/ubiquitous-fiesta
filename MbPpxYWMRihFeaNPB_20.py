
def sum_of_evens(lst):
  result=0
  for x in lst:
    for y in x:
      if y%2==0:
        result=result+y
  return result

