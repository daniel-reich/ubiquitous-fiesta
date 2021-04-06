
def find_all_digits(nums):
  digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
  for i in nums:
    for j in str(i):
      if j in digits:
        digits.remove(j)
    if digits == []:
      return i
  return "Missing digits!"

