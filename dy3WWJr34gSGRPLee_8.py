
def make_box(n):
  result = []
  result.append('#'*n)
  for i in range(n - 2):
    result.append('#' + (' ' * (n-2)) + '#')
  if n > 1:
    result.append('#'*n)
  return result

