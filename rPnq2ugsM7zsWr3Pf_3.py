
def find_all_digits(nums):
  all_digits = set('0123456789')
  digits = set()
  for num in nums:
    digits.update(str(num))
    if digits == all_digits:
      return num
  return "Missing digits!"

