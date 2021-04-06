
def even_or_odd(s):
  od = sum(int(i) if i in "13579" else -int(i) for i in s)
  if not od:
    return 'Even and Odd are the same'
  if od > 0:
    return "Odd is greater than Even"
  return "Even is greater than Odd"

