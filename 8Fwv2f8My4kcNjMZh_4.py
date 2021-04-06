
class ones_threes_nines:
  
  def __init__(self,n):
    d={9:0,3:0,1:0}
    for i in [9,3,1]:
      while n>=i:
        d[i]+=1
        n-=i
    self.answer = 'nines:{d[9]}, threes:{d[3]}, ones:{d[1]}'.format(d=d)

