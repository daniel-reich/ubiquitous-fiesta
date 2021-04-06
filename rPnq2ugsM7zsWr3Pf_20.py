
def find_all_digits(nums):
  s = set()
  for n in nums:
    for d in str(n):
      s.add(d)
    if len(s) == 10:
      return n
  return 'Missing digits!'

