
def check(lst):
  nums = (n>lst[x] for x, n in enumerate(lst[1:]))
  return "increasing" if all(nums) else "decreasing" if not all(nums) else "neither"

