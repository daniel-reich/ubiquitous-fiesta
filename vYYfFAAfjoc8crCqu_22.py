
def tree(h):
  L = []
  for i in range(1,h*2,2):
    L.append("#" * i)
  FL = []
  for i in range(len(L)):
    FL.append(" "*(h-i-1) + L[i] + " "*(h-i-1))
  return FL

