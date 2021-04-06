
def ABA(s):
  s = ord(s)
  seed = 65
  string = ''
  while seed <= s:
    string = string + chr(seed) + string
    seed += 1
  return string

