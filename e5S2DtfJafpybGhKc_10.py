
def rotate(mat):
  ans = []
  for a in list(zip(*mat)):
    ans.append(list(reversed(a)))
  return ans

