
def left_digit(num):
  num=list(num)
  for x in num:
    try:
      x=int(x)
      return x
    except ValueError:
      continue

