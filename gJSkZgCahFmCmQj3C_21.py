
def de_nest(lst):
  l = lst[0] #Define 'l' so a while loop can be used
  while isinstance(l,list): #repeat until l is not a list
    l = l[0] 
    #This is a neat little trick in recursion, you can keep diving
    #into list by just taking the 0 index of itself!
  return l

