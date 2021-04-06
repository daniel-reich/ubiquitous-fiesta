
def skip_the_sugar(drinks):
  l=[]
  for i in range(len(drinks)):
    if drinks[i]!="cola" and drinks[i]!="fanta":
      l.append(drinks[i])
  return l

