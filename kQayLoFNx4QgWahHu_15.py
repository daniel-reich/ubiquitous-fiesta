
def order(lst):
  a = sorted(enumerate(lst), key=lambda x: x[1]) 
  return [i[0] for i in a]

