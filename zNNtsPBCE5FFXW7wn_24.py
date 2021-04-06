
def empty_values(lst):
  t = {int: 0, float: 0.0, str: "", bool: False,
       list: [], tuple: (), set: set(), type(None): None}
       
  for i, ele in enumerate(lst):
    lst[i] = t[type(ele)]
  
  return lst

