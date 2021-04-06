
def is_super_d(n):
  lst = list(map(lambda x: str(x * pow(n,x)),range(2,10)))
  targeted = ["22","333","4444","55555","666666","7777777","88888888","999999999"]
  numbers = zip(lst,targeted)
  
  for k,t in numbers:
    if t in k:
      return "Super-{} Number".format(targeted.index(t) + 2)
  return "Normal Number"

