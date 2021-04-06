
def is_palindrome_possible(txt):
  n = [txt.count(x) for x in set(txt)]
  if txt==txt[::-1]:  return True
  else: return n.count(1)==1 or all([i==2 for i in n])

