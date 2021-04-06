
def tune(lst):
  res=[]
  for a,b in zip(lst,[329.63, 246.94, 196, 146.83, 110, 82.41]):
    if abs(a-b)/b<0.005:res+=['OK']
    elif a==0:res+=[' - ']
    elif a>b and round(abs(a-b)/b,2)>=0.03:res+=['+<<']
    elif a>b:res+=['+<']
    elif a<b and round(abs(a-b)/b,2)>=0.03:res+=['>>+']
    else:res+=['>+']
  return res

