
def add_letters(a):
  if not a:
    return 'z'
  base = ord('a') - 1
  total = 0
  for letter in a:
    total = (total + ord(letter) - base) % 26
  if total == 0:
    return 'z'
  return chr(base + total)

