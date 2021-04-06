
def check(lst):
  i=0
  try:
    while i<len(lst)-2:
      if lst[i]>lst[i+1] and lst[i+1]>lst[i+2]:
        i+=1
        continue
      elif lst[i]<lst[i+1] and lst[i+1]<lst[i+2]:
        i+=1
        continue
      else:
        return 'neither'
        break
  except:
    pass
  if lst[1]>lst[0]:
    return 'increasing'
  elif lst[1]<lst[0]:
    return 'decreasing'
  else:
    return 'neither'

