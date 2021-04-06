
def is_equal(nums):
  S = lambda x: sum(int(i) for i in str(x))
  A, B = nums
  return S(A) == S(B)

