
def seq_level(lst):
  def transfo(l):
    return [l[i+1]-l[i] for i in range(len(l)-1)]
  n=1
  lst=transfo(lst)
  while len(set(lst))!=1:
    lst=transfo(lst)
    n+=1
  return {1: 'Linear', 2: 'Quadratic', 3: 'Cubic'}[n]

