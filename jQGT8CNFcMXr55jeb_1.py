
def numbers_sum(lst):
  return sum([i for i in lst if isinstance(i,int) and not isinstance(i,bool)])

