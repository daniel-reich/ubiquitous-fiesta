
def checker_board(n, el1, el2):
  if el1==el2: return "invalid"
  return [[el1 if(j%2and i%2)or(i%2==0and j%2==0) else el2 for j in range(1, n+1)]for i in range(1,n+1)]

