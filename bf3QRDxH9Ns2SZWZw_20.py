
def all_explode(grid):
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
    
  xpl(0,0)
​
  return sum([x.count('x')+x.count('+') for x in data]) ==0

