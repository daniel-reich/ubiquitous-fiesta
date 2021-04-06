
def func(lst):
  def elements(lst):
    return len(lst)
  
  summ = elements(lst)
  
  for item in lst:
    if isinstance(item, list) == True:
      summ += elements(item)
      for ite in item:
        if isinstance(ite, list) == True:
          summ += elements(ite)
          for it in ite:
            if isinstance(it, list) == True:
              summ += elements(it)
              for i in it:
                if isinstance(i, list) == True:
                  summ += elements(i)
                  for t in i:
                    if isinstance(t, list) == True:
                      summ += elements(t)
  
​
  return summ

