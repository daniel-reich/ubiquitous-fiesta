
def almost_uniform(nums: list) -> int:
  uniq_nums = set(nums)
  result = []
  for n in uniq_nums:
    if (n + 1) in uniq_nums:
      result.append(nums.count(n) + nums.count(n + 1))
  return 0 if len(result) == 0 else max(result)

