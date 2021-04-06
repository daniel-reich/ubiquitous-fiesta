
def generate_rug(n, direction):
  arr=[]
  for i in range(n):
    temp=[]
    if direction=="left":
      for j in range(n):
        temp.append(abs(i-j))
    elif direction=="right" :
      for j in range(n-1,-1,-1):
        temp.append(abs(i-j))
    arr.append(temp)
  return arr

