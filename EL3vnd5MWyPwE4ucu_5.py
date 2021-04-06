
def fibonacci(n):
  f = [0,1]
  count = 0
  while count < n:
    for num in range(1, len(f)):
      f.append(f[num]+f[num-1])
      f.remove(f[0])
      count += 1
  return str(f[0])

