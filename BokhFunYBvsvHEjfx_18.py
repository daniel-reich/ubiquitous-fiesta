
def seven_boom(lst):
  s=''
  for n in lst:
    s=s+str(n)
  if '7' in s:
    return "Boom!"
  else:
    return "there is no 7 in the list"

