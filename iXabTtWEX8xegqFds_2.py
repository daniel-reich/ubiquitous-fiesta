
def alternate_sort(lst):
  nums = sorted(i for i in lst if type(i) is int)
  chars = sorted(i for i in lst if type(i) is str)
  return [j for i in zip(nums, chars) for j in i]

