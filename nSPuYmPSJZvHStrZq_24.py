
def oddeven(lst):
  counteven=0
  countodd=0
  for a in range(0,len(lst)):
    if lst[a]%2!=0:
      counteven+=1
    else:
      countodd+=1
  if counteven>countodd:
    return True
  else:
    return False

