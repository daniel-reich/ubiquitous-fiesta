
def logarithm(base, num):
  count = 1
  while base != num:
    if base < 2 or num < base:
      return "Invalid"
    else:
      count += 1
      num = num/base
  return count

