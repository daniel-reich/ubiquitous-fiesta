
def letter_at_position(n):
  if n > 0:
    if int(n)==float(n):
      return chr(int(n)+96)
  return "invalid"

