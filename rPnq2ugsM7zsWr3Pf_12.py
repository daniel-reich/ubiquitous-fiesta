
def find_all_digits(nums):
  goal = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
  digs = set()
  
  for num in nums:
    l = list(str(num))
    for item in l:
      i = int(item)
      digs.add(i)
    
    if digs == goal:
      return num
​
  return "Missing digits!"

