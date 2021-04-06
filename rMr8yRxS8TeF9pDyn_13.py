
def war_of_numbers(lst):
  return max(sum([i for i in lst if i%2==0]),sum([i for i in lst if i%2==1]))-min(sum([i for i in lst if i%2==0]),sum([i for i in lst if i%2==1]))

