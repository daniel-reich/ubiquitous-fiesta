
def sum_odd_and_even(lst):
  return [sum(filter(lambda x:x%2==0,lst)),sum(filter(lambda x:x%2!=0,lst))]

