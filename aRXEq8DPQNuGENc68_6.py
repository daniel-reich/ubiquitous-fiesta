
def salt(t):
  from math import e
​
  salt = eval('1 + 9 * e ** -(0.1*t)')
​
  return round(salt, 3)

