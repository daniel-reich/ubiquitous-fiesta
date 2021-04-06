
def bomb(lst):
  a=[]
  for i in range(0,3):
   a.append(round(lst[i][2]**2*0.343**2))
  
  for x in range(51):
      for y in range(51):
         if  a[0]==((x-lst[0][0])**2 + (y-lst[0][1])**2) and a[1]==((x-lst[1][0])**2 + (y-lst[1][1])**2) and a[2]==((x-lst[2][0])**2 + (y-lst[2][1])**2):
          return (x,y)

