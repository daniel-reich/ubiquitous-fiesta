
def has_digit(txt):
  digits = '1234567890'
  for ch in txt:
    if ch in digits:
      return True
  else:
      return False

