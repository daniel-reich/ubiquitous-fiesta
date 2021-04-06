
def mode(nums):
  temp_set = set()
  for i in range(len(nums) - 1):
    if(nums[i] == nums[i + 1]):
      temp_set.add(nums[i])
  unique_multiples = list(temp_set)
  unique_multiples.sort()
  count = [0] * len(unique_multiples)
  for i in range(len(nums)):
    if nums[i] in unique_multiples:
      count[unique_multiples.index(nums[i])] += 1
  max_count = max(count)
  result = []
  for i in range(len(count)):
    if count[i] == max_count:
      result.append(unique_multiples[i])
  return result

