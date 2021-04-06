
def greater_than_sum(nums):
  sum1=0
  sum2=0
  for i in range(1,len(nums)):
      if nums[i]>sum(nums[:i]):
        sum1+=1
      else:
        sum2+=1
  return len(nums)-1==sum1

