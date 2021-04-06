
def print_all_groups():
  d=[]
  lst = ['a', 'b', 'c', 'd', 'e']
  for i in range(1,7):
    for j in lst:
      d.append(str(i)+j)
  return ', '.join(d)

