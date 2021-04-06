
def ends_add_to_10(nums):
  lst = list(map(str, map(abs, nums)))
  return sum(int(n[0])+int(n[-1]) == 10 for n in lst)

