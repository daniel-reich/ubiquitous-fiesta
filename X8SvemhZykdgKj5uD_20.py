
def letter_at_position(n):
  alph = "abcdefghijklmnopqrstuvwxyz"
  return alph[int(n-1)] if n % 1 == 0 and n >0 else "invalid"

