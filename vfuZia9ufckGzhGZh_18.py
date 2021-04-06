
def seq_level(lst, count=0):
  seq = {0: 'Linear', 1: 'Quadratic', 2: 'Cubic'}
  lst = [lst[i+1]-lst[i] for i in range(0,len(lst)-1)]
  if lst[0] == lst[1]:
    return seq[count]
  return seq_level(lst, count+1)

