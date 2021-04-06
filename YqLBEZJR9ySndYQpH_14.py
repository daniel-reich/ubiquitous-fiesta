
def staircase(n):
  shape=""
  if n>0:
    for i in range(n):
      for j in range(n):
        if i+j<n-1:
          shape+="_"
        else:
          shape+="#"
      shape+="\n"
    return shape[:-1]
    
  if n<0:
    n=abs(n)
    for i in range(n):
      for j in range(n):
        if i>j:
          shape+="_"
        else:
          shape+="#"
      shape+="\n"
    return shape[:-1]

