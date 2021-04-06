
def closest_palindrome(num):
  s = str(num)
  m = len(s)//2
  
  if s == s[::-1]:
    return num
  if s.rstrip('0') == '1':
    return num - 1
​
  if len(s)%2:
    return int(s[:m+1] + s[:m][::-1])
  return int(s[:m] + s[:m][::-1])

