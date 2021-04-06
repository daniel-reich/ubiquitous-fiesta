
def complete_square(lst):
  lst = [l+([0]*(len(lst)-len(lst[0]))) for l in lst]
  lst = lst+[[0]*len(lst[0])]*(len(lst[0])-len(lst))
  return lst

