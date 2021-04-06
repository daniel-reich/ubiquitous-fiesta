
def closest_palindrome(num):
  a = 0
  b = 0
  c = 1
  while str(num)!=str(num)[::-1]:
    a = str(num-c)
    if a==a[::-1]:
      return int(a)
    b = str(num+c)
    if b==b[::-1]:
      return int(b)
    c+=1
  return num

