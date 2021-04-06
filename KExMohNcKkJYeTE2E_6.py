
def is_orthogonal(first, second):
  sum = 0
  for i in range(0, len(first)):
    sum += first[i] * second[i]
  return sum == 0

