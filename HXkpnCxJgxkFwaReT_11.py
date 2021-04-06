
def count_datatypes(*args):
 x=[0,0,0,0,0,0]
 for i in args:
  if type(i)==int:
   x[0]=x[0]+1
  elif type(i)==str:
   x[1]=x[1]+1
  elif type(i)==bool:
   x[2]=x[2]+1
  elif type(i)==list:
   x[3]=x[3]+1
  elif type(i)==tuple:
   x[4]=x[4]+1
  elif type(i)==dict:
   x[5]=x[5]+1
 return x

