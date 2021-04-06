
def final_result(lst):
​
  poppable = True
​
  while poppable == True and lst != []:
    sn = None
    en = None
​
​
    for n in range(0, len(lst)):
    
      item = lst[n]
​
      try:
        nitem = lst[n + 1]
      except IndexError:
        poppable = False
​
      popped = False
      
      if poppable == True:
        if item == nitem:
          sn = n
​
          for num in range(n, len(lst)):
            
            titem = lst[num]
            if titem != item:
              en = num
              popped = True
              break 
          if popped == False and sn != None:
            en = len(lst)
            popped = True
        if popped == True:
          break
      
    try:
      for n in reversed(range(sn, en)):
        lst.pop(n)
    except TypeError:
      continue
    
  return lst

