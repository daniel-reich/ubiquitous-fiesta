
def find_all_digits(nums):
  s,j,combo = [str(i) for i in nums],0, ''
  while len(set(combo))<10:
    if j == len(nums):
      return 'Missing digits!'
    else:
      combo+=s[j]
      j+=1
  return nums[j-1]

