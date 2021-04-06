
def jazzify(lst):
  ls = []
  for i in lst:
    if i[-1] != '7':    
      ls.append(i + '7')
    else:
      ls.append(i)
  return ls

