
def find_all_digits(nums):
  k=[]
  for i in nums:
    for j in str(i):
      if(j not in k):
        k.append(j)
    if(len(k)==10):
      return i
  return "Missing digits!"

