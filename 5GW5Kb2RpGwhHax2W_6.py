
def spiral_transposition(lst):
  r=[]
  [r.append(i) for i in lst.pop(0)]
  while lst!=[]:
    lst=[[lst[h][i] for h in range(len(lst))] for i in range(len(lst[0]))][::-1]
    [r.append(i) for i in lst.pop(0)]
  return r

