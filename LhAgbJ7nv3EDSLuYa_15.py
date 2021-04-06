
def golomb(n):
  result = [1,2,2]
  for i in range(3, n+1):
    for j in range(result[i-1]):
      result.append(i)
      if len(result) == n: return result
  print(result)
  return result

