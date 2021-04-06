
def tree(h):
  ans = []
  row_len = 2*h-1
  for i in range(1, row_len+1, 2):
    n = (row_len - i)//2
    row = ' '*n + '#'*i + ' '*n
    ans.append(row)
  return ans

