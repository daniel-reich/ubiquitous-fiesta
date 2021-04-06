
def checker_board(n, el1, el2):
  lst = [el1,el2]*n*(n//2+1)
  lst = lst[:n*n]
  result = [lst[n*i:n*i+n] for i in range(n)]
  if el1 != el2:
    return [x[::-1] if i%2 else x for i,x in enumerate(result)]
  return 'invalid'

