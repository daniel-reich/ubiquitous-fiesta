
def countdown(n, in_str):
  upper_str = in_str.upper()
  new_sen = ""
  while n > 0:
    new_sen += str(n) + ". "
    n = n - 1
  new_sen += upper_str + "!"
  return new_sen

