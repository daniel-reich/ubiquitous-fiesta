
def pascals_triangle(n: int) -> list:
  if n == 1: return [1]
  result = [1]; prev = [1]
  for i in range(1, n):
    next = [1]
    for j in range(i - 1):
      next.append(prev[j] + prev[j + 1])
    next.append(1)
    result.extend(next)
    prev = next
  return result

