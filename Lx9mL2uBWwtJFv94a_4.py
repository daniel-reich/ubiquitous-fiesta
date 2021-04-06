
def checker_board(n, e1, e2):
  
  if e1 == e2:
    return 'invalid'
  
  else:
    return [([e1,e2]*n)[:n] if i%2 else ([e1,e2]*n)[1:n+1] for i in range(1,n+1)]

