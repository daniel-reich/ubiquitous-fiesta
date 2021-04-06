
def sum_odd_and_even(l):
  o=sum(x for x in l if x%2)
  return[sum(l)-o,o]

