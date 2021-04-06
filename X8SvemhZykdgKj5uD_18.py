
def letter_at_position(n):
  if n != int(n) or n < 1 or n > 26:
    return 'invalid'
  n = int(n)
  a = "abcdefghijklmnopqrstuvwxyz"
  return a[n-1]

