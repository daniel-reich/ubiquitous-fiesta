
def letter_at_position(n):
  return chr(int(n)+96) if 0<n<27 and n%1==0 else 'invalid'

