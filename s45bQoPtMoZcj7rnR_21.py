
def closest_palindrome(n):
  for i in range(n*10):
    if is_palindrome(n-i):
      return n-i
    if is_palindrome(n+i):
      return n+i
  
def is_palindrome(n):
  return str(n) == str(n)[::-1]

