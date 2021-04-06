
def find_all_digits(nums):
  found_digits = []
  for num in map(str, nums):
    for digit in num:
      if digit not in found_digits:
        found_digits.append(digit)
    if len(found_digits) >= 10:
      return int(num)
  return 'Missing digits!'

