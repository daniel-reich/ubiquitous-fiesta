
def letter_at_position(n):
  try:
    if n<1 or n>26 or (not n==int(n)):
      return "invalid"
    else:
      n=int(n)
      alphabet=[char for char in "abcdefghijklmnopqrstuvwxyz"]
      return alphabet[n-1]
  except TypeError:
    return "invalid"

