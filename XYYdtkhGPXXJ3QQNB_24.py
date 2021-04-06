
def contains_num(s):
  nums = [str(x) for x in range(10)]
  for x in nums:
    if x in s:
      return True
  return False
​
def num_in_str(lst):
  return [s for s in lst if contains_num(s)]

