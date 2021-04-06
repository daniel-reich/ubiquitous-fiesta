
def factor_sort(nums):
  lst = [(num,get_factors(num)) for num in nums]
  val = [[j[0] for j in lst if j[1] == i] for i in range(max(dict(lst).values())+1)]
  return [n for i in val for n in sorted(i)][::-1]
​
def get_factors(num):
  return sum(not num%i for i in range(1,num+1))

