
def column_chart(prodA, prodB, target):
  h = 1+max(t//10 for t in target)
  raw = [["  " for j in range(7)] for i in range(h)]
  for l in range(7):
    for k in range(prodA[l]//10):
      raw[k][l] = "++"
  for l in range(7):
    for k in range(prodA[l]//10,(prodA[l]+prodB[l])//10):
      raw[k][l] = "**"
  for l in range(7):
    raw[target[l]//10][l] = "__"
    
  raw = [" ".join([str((i+1)*10)]+["|"]+raw[i]+["|"]) for i in range(h)]
  
  raw = ["   | Mo Tu We Th Fr Sa Su |"] + raw
  
  return "\n".join(raw[::-1])

