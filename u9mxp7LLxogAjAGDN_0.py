
def factor_sort(nums):
  nums=sorted([[factors(i),i] for i in nums])[::-1]
  return [i[1] for i in nums]
def factors(num):
  return len([i for i in range(1,num+1) if num%i==0])

