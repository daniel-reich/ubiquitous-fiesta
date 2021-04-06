
def mode(nums):
  num_counts = {}
  for num in nums:
    if num not in num_counts:
      num_counts[num] = 1
    else:
      num_counts[num] += 1
      
  max_count = 0
  for key, count in num_counts.items():
    if count > max_count:
      max_count = count
      
  result = []
  for key, count in num_counts.items():
    if count == max_count:
      result.append(key)
  
  return sorted(result)

