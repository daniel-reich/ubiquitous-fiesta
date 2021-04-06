
def print_list(n):
  # shorter solution
  # return list(range(1, n + 1))
  result = []
  i = 1
  while i <= n:
    result += [i]
    i += 1
  return result

