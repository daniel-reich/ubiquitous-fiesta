
res=[]
def move(mat):
  global res
  res = mat[:]
  def F(direction):
    global res
    if direction=='stop':return res
    elif direction=='up':
      res=res[1:]+[res[0]]
      return F
    elif direction=='down':
      res=[res[-1]]+res[:-1]
      return F
    elif direction=='left':
      for i in range(len(res)):
        res[i]=res[i][1:]+[res[i][0]]
      return F
    elif direction=='right':
      for i in range(len(res)):
        res[i]=[res[i][-1]]+res[i][:-1]
      return F
  return F

