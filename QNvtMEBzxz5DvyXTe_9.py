
uppercase = {chr(i + 65) for i in range(26)}
lowercase = {chr(i + 97) for i in range(26)}
digits = {chr(i + 48) for i in range(10)}
special = {'!', '@', '#', '$', '%', '^', '&' '*', '(', ')', '-', '+'}
​
ALL = 0b1111
HAS_UPPER = 0b0001
HAS_LOWER = 0b0010
HAS_DIGIT = 0b0100
HAS_SPECIAL = 0b1000
​
def strong_password(password):
  needed = 0
  flags = 0
  
  for c in password:
    if flags == ALL:
      break
    if c in uppercase:
      flags |= HAS_UPPER
    if c in lowercase:
      flags |= HAS_LOWER
    if c in digits:
      flags |= HAS_DIGIT
    if c in special:
      flags |= HAS_SPECIAL
  
  flags ^= ALL
  
  while flags:
    needed += flags & 1
    flags >>= 1
  
  needed += max(max(6 - len(password), 0) - needed, 0)
  
  return needed

