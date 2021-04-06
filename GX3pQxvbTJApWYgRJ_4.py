
def is_kaprekar(n):
 kap=str(n**2)
 #print('kap',kap,type(kap))
 if len(kap) != 1:
  left=kap[0:len(kap)//2]
  #print('left',left)
  right=kap[len(kap)//2::]
  #print('right',right)
  total=int(left)+int(right)
 else:
  total=int(kap)
 if total==n: 
  return True
 else:
  return False

