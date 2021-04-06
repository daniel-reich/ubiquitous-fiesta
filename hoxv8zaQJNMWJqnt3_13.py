
# f**ck the recursion if there is obvious non recursive simplier solution
#  and recursivity check is poorly written :)
def is_heteromecic(n):
  i = 0
  while i*i+i < n: i += 1
  return i*i+i == n

