
def complete_binary(s):
  r = s[::-1]
  while len(r) % 8 != 0:
    r += '0'
  return r[::-1]

