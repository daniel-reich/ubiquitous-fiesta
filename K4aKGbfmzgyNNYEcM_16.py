
def is_shape_possible(n, angles):
  a=len(angles)
  sum1=0
  totAng=(n-2)*180
  if(n<3):
    return False
  else:
    for i in range(0,a):
      if(angles[i]>180):
        return False
      else:
        sum1=sum1+angles[i]
  if(sum1!=totAng):
    return False
  return True

