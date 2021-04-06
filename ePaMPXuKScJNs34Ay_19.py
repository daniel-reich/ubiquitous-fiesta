
def add_it_up(lst):
  for eachlist in lst:
    if type(eachlist) is list:
      return sum(lst,[])
    elif type(eachlist) is tuple:
      return sum(lst,())
  return sum(lst)

