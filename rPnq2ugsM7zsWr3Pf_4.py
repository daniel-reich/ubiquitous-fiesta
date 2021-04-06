
def find_all_digits(nums):
  strnums = [str(i) for i in nums]
  found = []
  for i in range(10):
    found.append(False)
  for num in strnums:
    for i in num:
      print(i)
      found[int(i)] = True
    if (not False in found):
      return int(num)
  return "Missing digits!"

