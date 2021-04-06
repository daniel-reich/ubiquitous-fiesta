
digits = "0123456789"
​
def trouble(num1, num2):
  for d in digits:
    if d*3 in str(num1) and d*2 in str(num2): return True
  return False

