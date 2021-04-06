
def get_discounts(nums, d):
 d=d.strip('%')
 disc=int(d)
 res=[]
 for i in nums:
  discount=(i*disc)/100
​
  res.append(discount)
 return res

