
def generate_rug(n):
  count = 0
  result = [[0]]
  for i in range(0, n-1, 2):
    count += 1
    for j in range(len(result)):
      result[j] = [count] + result[j] + [count]
    result = [[count for x in range(len(result[0]))]] + result + [[count for x in range(len(result[0]))]]
  return result

