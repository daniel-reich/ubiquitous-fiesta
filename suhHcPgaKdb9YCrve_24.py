
def even_or_odd(s):
  evenSum=0
  oddSum=0
  for i in s:
    if int(i)%2==0:
      evenSum+=int(i)
    else:
      oddSum+=int(i)
  if evenSum>oddSum:
    return "Even is greater than Odd"
  if evenSum<oddSum:
    return "Odd is greater than Even"
  if evenSum==oddSum:
    return "Even and Odd are the same"

