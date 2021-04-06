
def palindrome_descendant(num):
  while len(str(num))>=2:
    if isPalindrom(num):
      return True
    else:
      num = desc(num)
  return False
  
​
​
​
def desc(n):
  m = [int(i) for i in str(n)]
  return int(''.join(str(sum(m[i:i+2])) for i in range(0,len(m),2)))
​
def isPalindrom(n):
  return str(n)==str(n)[-1::-1]

