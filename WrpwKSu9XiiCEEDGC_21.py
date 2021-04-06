
def can_alternate(s):
  count = 0
  count1 = 0
  for x in s:
    if x == '0':
      count+=1
    if x == '1':
      count1+=1
  if count1 == count or count1 == count + 1 or count == count1 + 1:
    return True
  else:
    return False

