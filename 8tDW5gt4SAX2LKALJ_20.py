
def min_bombs_needed(grid):
  data=grid#.copy()
  
  def xpl(a,b):
​
    if a<0 or b<0: return None
    if a>=len(data) or b>=len(data[0]):return None
    if data[a][b]=='x':
      data[a][b]="X"
      xpl(a-1,b-1)
      xpl(a-1,b+1)
      xpl(a+1,b-1)
      xpl(a+1,b+1)
    if data[a][b]=='+':
      data[a][b]="T"
      xpl(a-1,b)
      xpl(a+1,b)
      xpl(a,b-1)
      xpl(a,b+1)
  
  def getx():
    for i,x in enumerate(data):
      if 'x' in x:
        return [i,x.index('x')]
      if '+' in x:
        return [i,x.index('+')]
    return [-1,-1]
  
  for i in range(10):
    [a,b]=getx()
    print(a,b)
    xpl(a,b)
    if sum([x.count('x')+x.count('+') for x in data]) ==0: return i+1

