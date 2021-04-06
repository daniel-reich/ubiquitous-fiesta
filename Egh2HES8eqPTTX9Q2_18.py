
def rolling_cipher(string, n):
  alpha2 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
​
  if n < 0:
    n += 26
  
  return alpha2[(alpha2.find(string[0]) + n) : (alpha2.find(string[0]) + n + 4)]

