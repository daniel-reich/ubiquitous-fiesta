
def collect(s, n):
  return sorted("".join(s[i*n+j] for j in range(n)) for i in range(len(s)//n))

