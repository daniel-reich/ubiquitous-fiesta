
def number_len_sort(lst):
  nums = []
  for i in lst:
    nums.append(str(i))
  x=  sorted(nums, key=len)
  return [int(y) for y in x]

