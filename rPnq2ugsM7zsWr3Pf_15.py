
def find_all_digits(nums):
  a = []
  b = [str(i) for i in list(range(0, 10))]
  
  for i in nums:
    for j in str(i):
      if j not in a:
        a.append(j)
    if sorted(a) == b:
      return i
​
  return 'Missing digits!'

