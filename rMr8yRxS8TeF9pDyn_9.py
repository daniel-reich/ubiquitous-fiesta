
def war_of_numbers(lst):
  return abs(sum([i for i in lst if i%2==0]) - sum([i for i in lst if i%2!=0]))

