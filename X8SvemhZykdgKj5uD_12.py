
def letter_at_position(n):
  return ''.join(chr(int(n)+96) if n-1 in range(26) else 'invalid' )

