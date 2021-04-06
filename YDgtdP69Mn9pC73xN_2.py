
def num_grid(lst):
  def check(i,j):
    s=0
    for ii in range(3):
        if not((0<=(i-1+ii)<=4)): continue
        for jj in range(3):
            if not((0<=(j-1+jj)<=4)): continue
            if lst[i-1+ii][j-1+jj]=='#': s+=1
        
    return s
​
​
​
  for i in range(5):
      for j in range(5):
          if lst[i][j]!='#':
              print(i,j,check(i,j))
              lst[i][j]=str(check(i,j))
  return lst

