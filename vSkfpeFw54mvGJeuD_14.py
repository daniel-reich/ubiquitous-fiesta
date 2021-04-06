
def lychrel(n, s = 0):
  if s == 500: 
    return True
  if is_palindrome(n): 
    return s
  return lychrel(n + int(str(n)[::-1]), s+1)
​
def is_palindrome(s):
  return str(s) == str(s)[::-1]

