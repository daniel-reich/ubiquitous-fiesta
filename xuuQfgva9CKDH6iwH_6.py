
def simulate_grass(g, x, y):
  arr = [[j for j in i] for i in g]
  arr[x][y] = "+"
  while True:
    changes = 0
    for i in range(0,len(arr)):
      for j in range(0,len(arr[0])):
        if arr[i][j] == "o":
          if any(arr[a][b] == "+" for a,b in zip([i-1,i,i,i+1],[j,j-1,j+1,j])):
            arr[i][j] = "+"
            changes += 1
    if changes == 0:
      return [''.join(j for j in i) for i in arr]

