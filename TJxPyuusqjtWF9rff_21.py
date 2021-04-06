
def get_only_evens(nums):
  numscopy = list.copy(nums)
  output = []
  for num in numscopy:
    if num % 2 == 0:
      if nums.index(num)%2 == 0:
        output.append(num)
        numscopy.remove(num)
        
  
  return output

