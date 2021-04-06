
def letter_at_position(n):
  if float(n) != float(int(n)) or (n < 1 or n > 26):
    return 'invalid'
  return chr(int(n+96))

