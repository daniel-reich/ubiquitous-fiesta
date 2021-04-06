
def longest_slide(pyramid):
  for i in range(len(pyramid)-2,-1,-1):
    for j in range(len(pyramid[i])):
      if pyramid[i+1][j]<pyramid[i+1][j+1]:
        pyramid[i][j]+=pyramid[i+1][j+1]
      else:
        pyramid[i][j]+=pyramid[i+1][j]
  return pyramid[0][0]

