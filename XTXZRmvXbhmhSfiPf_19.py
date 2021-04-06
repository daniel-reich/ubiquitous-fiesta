
def single_number(nums):
  
  Unique = set(nums)
  Seeking = sorted(list(Unique))
  
  Counter = 0
  Length = len(Seeking)
  
  while (Counter < Length):
    Item = Seeking[Counter]
    Events = nums.count(Item)
    
    if (Events == 1):
      return Item
    else:
      Counter += 1
  
  return "No unique items :-)"

