
def junction_or_self(n):
  result = []
  for i in range(n):
    if i + sum(map(int, str(i))) == n:
      result.append(i)
  return result[::-1] if len(result) > 0 else 'Self'

