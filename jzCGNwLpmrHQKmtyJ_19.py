
def parity_analysis(num):
  s = str(num)
  res = 0
  for i in s:
    res += int(i)
  
  return num%2 == res%2

