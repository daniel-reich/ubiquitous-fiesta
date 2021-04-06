
def is_icecream_sandwich(txt):
  newlist = []
  if len(txt) < 3:
    return False
  count = 0
  for i in txt:
    if i == txt[0]:
      count += 1
    else:
      newlist.append(i)
  if count % 2 == 0:
    set(newlist)
    if len(newlist) == 1:
      return True
  
    elif newlist[0] != newlist[1]:
      return False
    return True
    
  else:
    return False

