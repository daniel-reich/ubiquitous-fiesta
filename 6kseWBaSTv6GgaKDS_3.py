
def next_letters(s):
  for i in range(len(s) - 1, -1, -1):
    if s[i] != 'Z':
      return s[:i] + chr(ord(s[i]) + 1) + 'A'*(len(s)-i-1)
  return 'A'*(len(s)+1)

