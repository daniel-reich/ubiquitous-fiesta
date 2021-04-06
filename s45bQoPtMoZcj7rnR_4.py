
def closest_palindrome(num):
  a = b = num
  while True:
    if str(a) == str(a)[::-1]:
      return a
    a -=  1
    if str(b) == str(b)[::-1]:
      return b
    b += 1

