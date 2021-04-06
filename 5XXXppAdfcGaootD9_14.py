
def sum_odd_and_even(lst):
  return [sum([x for x in lst if x%2==0]),sum([x for x in lst if x%2!=0])]

