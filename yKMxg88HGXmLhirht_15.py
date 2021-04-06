
def add_letters(a):
  total = sum(ord(i) - 96 for i in a) % 26
  return chr(96 + total) if total else 'z'

