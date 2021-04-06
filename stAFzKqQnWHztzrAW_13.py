
def add_nums(nums):
  n_splt = nums.split(",")
  n_int = []
  for i in n_splt:
    n_int.append(int(i))
  return sum(n_int)

