
def can_traverse(x):
  hts = [sum(x[i][j] for i in range(len(x))) for j in range(len(x[0]))]
  return all(abs(hts[i]-hts[i-1])<2 for i in range(1,len(hts)))

