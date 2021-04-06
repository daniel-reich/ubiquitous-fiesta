
def closest_palindrome(num):
  i = 0
  while True:
    a, b = num + i, num - i
    if palindrome(a) or palindrome(b):
      return b if palindrome(b) else a
    i += 1
  
def palindrome(n):
  return str(n) == str(n)[::-1]

