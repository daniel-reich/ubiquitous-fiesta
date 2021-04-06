
import math
​
def happy(n):
  return happy_recursive(n)
​
​
def happy_recursive(n):
  n = str(n)
  digitsSum = 0
  for digit in n:
    digitsSum+=math.pow(int(digit),2)
  n = int(digitsSum)
  if n == 1:
    return True
  else:
    try:
      return happy_recursive(n)
    except Exception:
      return False

