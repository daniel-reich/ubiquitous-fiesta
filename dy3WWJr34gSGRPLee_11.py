
def make_box(n):
  box = []
  box.append("#"*n)
  for i in range(n-2):
    box.append("#" + " " * (n-2) + "#")
  
  box.append("#"*n)
  if n == 1: 
    return ["#"]
  else: 
    return box

