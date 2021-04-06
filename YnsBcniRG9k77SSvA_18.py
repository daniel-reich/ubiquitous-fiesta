
def print_all_groups():
  nums = ['1','2','3','4','5','6']
  char = ['a','b','c','d','e']
  combined = []
  for i in nums:
    for j in char:
      combined.append(i+j)
  return ', '.join(combined)

