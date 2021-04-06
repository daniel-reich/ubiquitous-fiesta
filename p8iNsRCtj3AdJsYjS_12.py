
def title_to_number(s):
  result = 0
  power = len(s) - 1
  
  for i in s:
    tmp = toInt(i)
    result += tmp * (26 ** power)
    power -= 1
  return result
​
def toInt(s):
  return ord(s) - 64

