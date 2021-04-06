
def sum_of_evens(lst):
  return sum(i for j in lst for i in j if i%2==0)

