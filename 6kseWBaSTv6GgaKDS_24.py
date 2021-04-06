
def next_letters(s):
  if not s: return "A"
  a = ord('A')
  z = ord('Z')
​
  s = [ord(x) for x in s]
​
  s[-1] += 1
  
  while z + 1 in s:
    if s[0] == z + 1: #add location in front
      s[0] = a
      s = [a] + s
​
    for i in range(len(s)):
      if s[-i] == z + 1: #overflow to prev digits
        s[-i] = a
        s[-i-1] += 1
  
  s = [chr(x) for x in s]
  
  return ''.join(s)

