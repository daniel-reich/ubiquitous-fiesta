
def take_second(elem):
    return elem[1]
    
def get_best_student(g):
  a=[]
  for i in g:
    a.append([i, sum(g[i])/len(g[i])])
  return sorted(a, key=take_second)[-1][0]

