
def flip_list(lst):
  if (lst==[]):return []
  elif (isinstance(lst[0],int)):
    return [[i] for i in lst]
  else:
    return [j for i in lst for j in i]

