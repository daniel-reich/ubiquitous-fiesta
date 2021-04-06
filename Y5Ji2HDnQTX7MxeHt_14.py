
def snakefill(n):
  snake = 1
  ans = 0
  while(True):
    snake = snake*2
    if snake <= n*n: ans+=1
    else: break
  return ans

