
def mult_table(n):
​
  res = []
  index = 1
​
  while len(res) != n:
    res.append([i for i in range(index, n * index + 1, index)])
    index += 1
  
  return res

