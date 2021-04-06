
def check_palindrome(num):
  if str(num) == str(num)[::-1]:
    return True
  return False
​
def closest_palindrome(num):
  if check_palindrome(num):
    return num
  else:
    num1 = num ; num2 = num
    while True:
      num1 = num1 - 1
      if check_palindrome(num1):
        diff1 = num - num1
        break
    while True:
      num2 = num2 + 1
      if check_palindrome(num2):
        diff2 = num2 - num
        break
    if diff1 > diff2:
      return num2
    elif diff1 < diff2:
      return num1
    else:
      return num1

