
def letter_at_position(n):
  alpha = list("abcdefghijklmnopqrstuvwxyz")
  if n % 1 != 0:
    return "invalid"
  else:
    n = int(n)
    if n < 1:
      return "invalid"
    return (alpha[n-1])

