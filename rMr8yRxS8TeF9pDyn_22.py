
def war_of_numbers(lst):
  even = sum(i for i in lst if i%2==0)
  odd = sum(i for i in lst if i%2!=0)
  return abs(even-odd)

