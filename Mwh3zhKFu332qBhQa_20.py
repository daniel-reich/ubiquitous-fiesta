
def guess_sequence(n):
  result = [30]
  for i in range(n):
    result.append(result[i]+60)
  return sum(result[1:])

