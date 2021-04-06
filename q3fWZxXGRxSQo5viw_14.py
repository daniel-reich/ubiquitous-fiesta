
def cal(depth):
  t=0
  if depth>150:
    z=depth//150  
    t=z*6+z*10+30*z
    if (depth%150)%5 !=0:
      t=t+((depth%150)//5)+1
      return t
    else:
      t=t+((depth%150)/5)
      return t
  else:
    if depth%5 ==0:
      return depth/5
    else:
      return (depth//5)+1

