
def row_sum(n):
  cur = 1
  row = 0
  length = 1
  for i in range(n):
    row = sum(range(cur,cur+length))
    cur+=length
    length+=1
  return row

