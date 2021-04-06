
from collections import Counter as C
def single_number(nums):
  A=dict(C(nums))
  for x in A:
    if A[x]==1:
      return x

