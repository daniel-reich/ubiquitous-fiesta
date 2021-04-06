
def special_reverse(s, c):
  s = s.split()
  return ' '.join(word[::-1] if word.startswith(c) else word for word in s)

