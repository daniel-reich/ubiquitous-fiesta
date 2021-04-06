
def generate_nonconsecutive(n):
  res = '0' * n
  for i in range(1, pow(2, n)):
      s = bin(i)[2:]
      s= '0' * (n -len(s)) + s
      if '11' not in s:
          res += ' ' + s
  return res

