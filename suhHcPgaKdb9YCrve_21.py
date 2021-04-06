
def even_or_odd(s):
  evens=sum([int(i) for i in s if int(i)%2==0])
  odds=sum([int(i) for i in s if int(i)%2!=0])
  if evens>odds:
    return"Even is greater than Odd"
  if evens<odds:
    return"Odd is greater than Even"
  return"Even and Odd are the same"

