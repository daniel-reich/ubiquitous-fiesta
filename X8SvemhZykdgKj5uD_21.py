
def letter_at_position(n):
  if not 1 <= n <= 26 or n != int(n):
    return 'invalid'
  else:
    return chr(96 + int(n))

