
def longest_slide(pyramid):
  pyr = pyramid[::-1]
  for i in range(1,len(pyr)):
    for j in range(len(pyr[i])):
      pyr[i][j] = pyr[i][j]+max(pyr[i-1][j],pyr[i-1][j+1])
  return pyr[-1][-1]

