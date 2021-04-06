
def war_of_numbers(lst):
  return abs(sum(lst)-2*sum(i for i in lst if i%2==0))

