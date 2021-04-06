
def alternate_sort(lst):
  chars = sorted(i for i in lst if isinstance(i, str))
  nums = sorted(i for i in lst if isinstance(i, int))
  return [i for p in zip(nums, chars) for i in p]

