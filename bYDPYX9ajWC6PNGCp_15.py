
def track_robot(*arguments):
  expr=[]
  for x in arguments:
    expr.append(x)
  a=0
  b=0
  isk=False
  isky=False
  for i in range(0,len(expr)):
    if i % 2==0 and isk==False:
      isk = True
      a+=expr[i]
    elif i%2==0 and isk == True:
      isk=False
      a-=expr[i]
    elif i%2!=0 and isky ==False:
      isky=True
      b+=expr[i]
    elif i%2!=0 and isky ==True:
      isky=False
      b-=expr[i]
      
  return [b,a]

