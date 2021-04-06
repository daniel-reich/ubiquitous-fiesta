
def snakefill(n):
  snake_len = 1
  fields = n * n
  count = 0
  while(True):
    tmp = snake_len * 2
    if(tmp > fields): break
    snake_len = tmp
    count += 1
  return count

