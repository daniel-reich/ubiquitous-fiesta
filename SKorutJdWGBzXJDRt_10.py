
def greet_people(names):
  res=""
  if len(names)==1:
    res+="Hello "+names[0]
  else: 
    for i in range(len(names)):
      if i!=len(names)-1:
        res=res+"Hello "+names[i]+", "
      else:
        res=res+"Hello "+names[i]
  return res

