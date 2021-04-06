
def sum_odd_and_even(lst):
  return [sum(i for i in lst if i%2==0), sum(i for i in lst if i%2==1)]

