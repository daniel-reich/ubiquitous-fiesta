
def almost_uniform(nums):
  count_dict = {}
  for n in nums:
    count_dict[n] = count_dict.get(n, 0) + 1
  sorted_count = sorted(count_dict.items())
  diffs = [sorted_count[i + 1][1] + sorted_count[i][1] for i in range(len(sorted_count) - 1) if sorted_count[i + 1][0] - sorted_count[i][0] == 1]
  return max(diffs) if len(diffs) > 0 else 0

