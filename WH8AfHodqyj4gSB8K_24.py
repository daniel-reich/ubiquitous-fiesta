
def is_authentic_skewer(s):
  a = s.count('-')
  if a == 0:
    return False
  b = s[0]
  c = s[-1]
  d = 0
  vowels = ['A', 'E', 'I', 'O', 'U']
  letters = list(s)
  letters2 = list(s)
  for i in range(a):
    letters.remove('-')
  if b in vowels:
    return False
  elif c in vowels:
    return False
  for i in range(len(letters)):
    if i % 2 != 0:
      if letters[i] not in vowels:
        return False
  for i in range(1, len(letters2)):
    if letters2[i] not in letters:
      d += 1
    else:
      break
  if a % d != 0:
    return False
  else:
    return True

