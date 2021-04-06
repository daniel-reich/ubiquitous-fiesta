
def sum_of_holes(N):
  final = 0
  for i in range(1, N+1):
    for j in str(i):
      if j in '0469':
        final += 1
      elif j == '8':
        final += 2
  return final

