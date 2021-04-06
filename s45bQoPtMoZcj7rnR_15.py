
def closest_palindrome(num):
  a = b = num
  while 1:
    if str(a) == str(a)[::-1]:
      return a
    if str(b) == str(b)[::-1]:
      return b
    a -= 1
    b += 1

