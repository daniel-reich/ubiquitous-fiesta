
def makeBox(n):
  if n==1:
    return ["#"]
  num_itr = n - 2
  box = ["#"*n]
  for itr in range(num_itr):
    box.append("#"+" "*num_itr+"#")
  box.append("#"*n)
  return box

