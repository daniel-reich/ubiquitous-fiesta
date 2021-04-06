
def find_missing(lst):
 if lst is None or len(lst)==0:
  return False
 else:
  listlen= sorted([len(i) for i in lst])
  if 0 in listlen:
   return False
  else:
   for j in range(listlen[0],listlen[-1]):
    if j not in listlen:
     return j

