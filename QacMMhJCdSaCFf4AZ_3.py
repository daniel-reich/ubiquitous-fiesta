
import math
# For any arithmetic or geometric integer sequence given (starting with the first element), return a formula that generates numbers for that sequence. Return False if neither arithmatic or geometric. Input sequence will be at least 5 terms long.
​
def sequence_generator(seq):
  # find whether sequence is geometric or arithmatic
  commonRatio = [seq[i+1]/seq[i] for i in range(len(seq)-1)]
  cr_set = set(commonRatio)
  l_crs = len(cr_set)
  c1 = int(cr_set.pop())
  ft1 = seq[0]//c1
  # print(f"seq: {seq} commonRatio: {commonRatio} cr_set: {cr_set} l_crs: {l_crs} c1: {c1} ft1: {ft1}")
​
  commonDiff = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
  cd_set = set(commonDiff)
  l_cds = len(cd_set)
  c2 = cd_set.pop()
  ft2 = seq[0] - c2
  # print(f"seq: {seq} commonDiff: {commonDiff} cd_set: {cd_set} l_cds: {l_cds} c2: {c2} ft2: {ft2}")
​
  def geometric(n):
    return (c1**n) * ft1
  
  def arithmatic(n):
    return c2*n + ft2
​
  return geometric if l_crs == 1 else arithmatic if l_cds == 1 else False

