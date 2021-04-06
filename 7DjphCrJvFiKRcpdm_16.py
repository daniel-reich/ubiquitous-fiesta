
def covered_integers(lst):
  count = 0
  nums = set()
  for i in lst:
    low = i[0]
    high = i[1]
    for i in range(low, high+1):
      nums.add(i)
  return len(nums)

