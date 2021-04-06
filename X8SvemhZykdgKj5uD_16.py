
def letter_at_position(n):
  if n != int(n) or not n in range(1,27): return "invalid"
  return chr(96 + int(n))

