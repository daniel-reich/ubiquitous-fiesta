
def seq(lst):
  konar=[]
  for i in range(len(lst[:-1])):
    konar.append(lst[i+1]-lst[i])
  return konar
def same(lst):
  return lst[1:][0]==lst[0]
​
def seq1(lst):
  if same(lst):
    return 0
  else:
    return 1+seq1(seq(lst))
    
def seq_level(lst):
  num=seq1(lst)
  if num==1:
    return 'Linear'
  elif num==2:
    return 'Quadratic'
  elif num==3:
    return "Cubic"

