
import numpy as np;
def printgrid(rows, cols):
  G = np.zeros((rows,cols));
  for i in range(cols):
    for j in range(rows):
      G[j,i] = i*rows+j+1;
  print(G);
  return G.tolist();

