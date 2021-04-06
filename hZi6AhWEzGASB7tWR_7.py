
def check(lst):
  if all(i<j for i,j in zip(lst,lst[1:])):
    return 'increasing'
  elif all(i>j for i,j in zip(lst,lst[1:])):
    return 'decreasing'
  else:
    return 'neither'

