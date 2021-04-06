
def mean(nums):
    
  Counter = 0
  Items = len(nums) - 1
  Length = len(nums)
  
  Sum = 0
  
  while (Counter < Length):
    Sum += nums[Counter]
    Counter += 1
    
  Mean = Sum/Length
  
  Answer = round(Mean,1)
  
  return Answer

