
def func(lst):  
  return (len(lst) + sum(func(el) for el in lst if isinstance(el, list))) if lst else 0

