
def letter_at_position(n):
  string = list("abcdefghijklmnopqrstuvwxyz")
  if type(n) == float:
    if str(n).endswith(".0"):
      return string[int(n)-1]
    else:
      return "invalid"
  elif n <= 0:
    return "invalid"
  else:
    return string[n-1]

