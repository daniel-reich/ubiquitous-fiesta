
def left_digit(num):
  for x in num:
    if x in "0123456789":
      return int(x)

