
def max_product(lst):
  s = sorted(lst)
  return max(s[-1]*s[-2]*s[-3],s[-1]*s[0]*s[1])
​
def min_product(lst):
  s = sorted(lst)
  return min(s[0]*s[1]*s[2],s[0]*s[-1]*s[-2])

