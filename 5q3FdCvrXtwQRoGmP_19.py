
def count_towers(towers):
  n=0
  m=[]
  for i in towers:
    i='  '.join(i)
    i = i.split(' ')
    n=i.count('##')
    n=str(n)
    m.append(n)
  n=[int(k) for k in m]
  return max(n)

