
def is_parallelogram(a):
 a1=a[1][0]-a[0][0]
 a2=a[2][0]-a[0][0]
 a3=a[2][0]-a[3][0]
 a4=a[1][0]-a[3][0]
 a5=a[3][0]-a[1][0]
 b1=a[1][1]-a[0][1]
 b2=a[2][1]-a[0][1]
 b3=a[2][1]-a[3][1]
 b4=a[1][1]-a[3][1]
 b5=a[3][1]-a[1][1]
 if(a1==a3 and b1==b3):
   return(True)
 elif(a2==a4 and b2==b4):
   return(True)
 elif(a2==a5 and b2==b5):
   return(True)
 else:
   return(False)

