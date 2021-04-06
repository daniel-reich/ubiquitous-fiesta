
def esthetic(decimal_number):
  aa=[[],[],[],[],[],[],[],[],[],[],[]];b=[];c=[]
  for i in range(2,11):
    a=decimal_number
    while a > 0:
        remainder = a % i
        aa[i].append(remainder)
        a = a // i
  for i ,j in enumerate(aa):
         if all((abs(j[k+1] - j[k])==1) for k in range(len(j)-1)):
               b.append(i)
         else: c.append(i)
  if len(c)==9:
      return ('Anti-Esthetic')
  else: return (b[2:])

