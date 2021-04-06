
def trans(lst):
    return list(zip(*lst))[::-1]
​
def spiral_matrix(side, string):
  IM=[[(i,j) for j in range(side)] for i in range(side)]
  lst2=[]
  while IM:
    lst2+=IM.pop(0)
    IM=trans(IM)
  lst3=lst2[::-1] 
  if len(string)<side*side:
    string=string+'+'*(side*side-len(string))
  else:
    string=string[:side*side]
  RE=[[0 for i in range(side)] for j in range(side)]
  for k in range(side*side):
    RE[lst3[k][0]][lst3[k][1]]=string[k]
  RT=[x[::-1] for x in RE]  
  return RE[::-1] if side%2==0 else RT

