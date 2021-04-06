
def first_one(a, b=None, c=None, d=None):
  list= [a,b,c,d]
  for x in list:
    if bool(x) == True:
      return x
  else:
    return "not found"

