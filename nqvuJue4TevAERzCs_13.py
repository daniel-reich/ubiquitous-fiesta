
def has_digit(txt):
  count=0
  temp=list(txt)
  for i in temp:
    if (i.isdigit()):
      count+=1
    else:
      pass
  return count>0

