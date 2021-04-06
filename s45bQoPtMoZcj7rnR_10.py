
def closest_palindrome(num):
  i = 0
  while True:
    left = num - i
    if str(left) == str(left)[::-1]:
      return left
    right = num + i
    if str(right) == str(right)[::-1]:
      return right
    i += 1

