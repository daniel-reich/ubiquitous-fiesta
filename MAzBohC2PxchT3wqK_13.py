
def shadow_sentence(a, b):
  alist, blist = a.split(' '), b.split(' ')
  if len(alist) != len(blist):
    return False
  
  j = -1
  for word in alist:
    j += 1
    if len(word) != len(blist[j]):
      return False
  
  i = -1
  for word in blist:
    i += 1
    for letter in word:
      if letter in alist[i]:
        return False
        
  return True

