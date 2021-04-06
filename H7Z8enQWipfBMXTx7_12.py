
def fib_str(n, f):
  answer=[f[0],f[1]]
  for i in range(n-2):
    answer.append(answer[-1]+answer[-2])
  return ', '.join(answer)

