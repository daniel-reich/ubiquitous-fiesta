
def sum_pairs(s):
  new = ''
  for i in range(0, len(s), 2):
    new += str(sum(int(j) for j in s[i:i+2]))
  return new
​
def palindrome_descendant(num):
  s = str(num)
  if len(s) < 3:
    return s == s[::-1]
  while len(s) > 2:
    s = sum_pairs(s)
    if s == s[::-1]:
      return True
  return False

