
def get_sum(num):
  total = 0
  txt = str(num)
  for dig in txt:
    total += int(dig)
  return total
​
def parity_analysis(num):
  digits = get_sum(num)
  
  return num%2 == digits%2

