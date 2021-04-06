
def next_number(num):
  digits = [int(c) for c in str(num)]
  result = next_number_r([], sorted(digits), digits)
  if result:
    return int(''.join([str(d) for d in result]))
  return num
def next_number_r(current, digits, minimum):
  if len(current) == len(minimum):
    return False
  for d in digits:
    if d < minimum[len(current)]:
      continue
    if d > minimum[len(current)]:
      next_digits = digits[:]
      next_digits.remove(d)
      if current + [d] + list(next_digits) != minimum:
        return current + [d] + list(next_digits)
      continue
    next = current + [d]
    next_digits = digits[:]
    next_digits.remove(d)
    result = next_number_r(current + [d], next_digits, minimum)
    if result:
      return result
  return False

