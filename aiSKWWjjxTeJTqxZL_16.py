
def complete_square(lst):
  if len(lst)>len(lst[0]):
    return [x+[0]*(len(lst)-len(lst[0])) for x in lst]
  elif len(lst)<len(lst[0]):
    return lst+[[0]*len(lst[0]) for x in range(len(lst[0])-len(lst))]
  else:
    return lst

