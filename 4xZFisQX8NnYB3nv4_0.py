
def maximum_seating(lst):
  lst = ['*', '*'] + lst + ['*', '*']
  seats = 0
  
  for i in range(2, len(lst) - 2):
    if 1 not in lst[i-2 : i+3]:
      seats += 1
      lst[i] = 1
      
  return seats

