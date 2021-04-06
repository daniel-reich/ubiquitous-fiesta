
def closest_palindrome(num):
  for i in range(150000000):
    if str(num-i) == str(num-i)[::-1]: return num-i
    if str(num+i) == str(num+i)[::-1]: return num+i

