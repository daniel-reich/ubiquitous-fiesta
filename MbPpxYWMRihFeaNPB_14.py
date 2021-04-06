
def sum_of_evens(lst):
  count=0
  for i in lst:
      for j in i:
        if j%2==0:
          count=count+j
          print(count)
  return count

