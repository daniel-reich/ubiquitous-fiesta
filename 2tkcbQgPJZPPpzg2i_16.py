
def sum_of_holes(N):
  return sum([1 if i in ['0', '4', '6', '9'] else (2 if i == '8' else 0)
  for i in "".join([str(i) for i in range(1, N+1)])])

