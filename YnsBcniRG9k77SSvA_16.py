
def print_all_groups():
  lst = ['a', 'b', 'c', 'd', 'e']
  return ', '.join([str(i) + k for i in range(1,7) for k in lst])

