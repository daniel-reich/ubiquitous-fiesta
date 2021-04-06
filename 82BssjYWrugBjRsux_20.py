
def index_multiplier(lst):
  myans = 0
  for i in range(len(lst)):
    myans += i*lst[i]
  return myans

