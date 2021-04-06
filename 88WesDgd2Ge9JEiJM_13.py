
def almost_uniform(nums):
  
  nums = sorted(nums)
  
  diff_1_substrings = []
  substring = []
  substring_val = None
  
  for n in range(len(nums)):
    num = nums[n]
    if substring_val == None:
      substring_val = num
    
    if num in [substring_val, substring_val + 1]:
      substring.append(num)
    elif num == substring_val + 2:
      diff_1_substrings.append(substring)
      substring = [s for s in substring if s == substring_val + 1]
      substring.append(num)
      substring_val = num-1
    else:
      diff_1_substrings.append(substring)
      substring = []
      substring_val = None
  
  if substring != []:
    diff_1_substrings.append(substring)
  #print(diff_1_substrings)
  lengths = [len(substring) for substring in diff_1_substrings if len(list(set(substring))) > 1]
  #print(lengths)
  
  try:
    return max(lengths)
  except ValueError:
    return len(lengths)

