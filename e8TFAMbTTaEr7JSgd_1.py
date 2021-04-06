
def left_digit(num):
  for ch in num:
    if ch.isdigit():
      return int(ch)

