
def generate_rug(n):
  if (n % 2) == 0 :
    return False
  if n == 1:
    return [[0]]
  elif n == 3 :
    return [[1,1,1],[1,0,1],[1,1,1]]
  else:
    mxv = n // 2
    answer = [[0 for x in range(n)] for y in range(n)]
    print(answer)
    for i in range(mxv+1):
      for j in range(mxv+1):
        cellval = max(abs(i-mxv),abs(j-mxv))
        answer[i][j] = cellval
        answer[-(i+1)][j] = cellval
        answer[-(i+1)][-(j+1)] = cellval
        answer[i][-(j+1)] = cellval
    answer[mxv][mxv] = 0
    return answer

