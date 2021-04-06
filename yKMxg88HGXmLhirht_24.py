
def add_letters(a):
  s = sum(ord(i)-96 for i in a)
  return chr(96+s%26) if s!=26 and a else 'z'

