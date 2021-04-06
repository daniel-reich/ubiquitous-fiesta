
def number_len_sort(lst):
  nums = [str(len(str(lst[i])))+str(i)+str(lst[i]) for i in range(len(lst))]
  nums.sort()
  for i in range(len(nums)):
    nums[i] = int(nums[i][2:])
  return nums

