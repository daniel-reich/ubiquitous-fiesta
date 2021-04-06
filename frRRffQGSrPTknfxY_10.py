
def digit_count(n):
  return int("".join(str(str(n).count(num)) for num in str(n)))

