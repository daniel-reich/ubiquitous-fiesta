
def harry(po: list) -> int:
  if len(po[0]) == 0: return -1
  po = [row[::-1] for row in po[::-1]] # flip matrix in both directions
  n = len(po)-1; m = len(po[0])-1
  for i in range(n):
    po[i+1][0] += po[i][0]
  for j in range(m):
    po[0][j+1] += po[0][j]
  # moving diagonally down the matrix...
  for k in range(min(n, m)):
    for i in range(n-k):
      po[i+k+1][k+1] += max(po[i+k+1][k], po[i+k][k+1])
    for j in range(m-k-1): # -1 to ensure no double-ups
      po[k+1][j+k+2] += max(po[k+1][j+k+1], po[k][j+k+2])
  return po[n][m]

