
def letter_at_position(n):
  return chr(int(n)+96) if 0<n<27 and not n%1 else 'invalid'

