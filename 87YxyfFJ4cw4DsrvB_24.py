
def generate_rug(n):
  return [[max(abs(i-(n-1)//2), abs(j-(n-1)//2))
            for i in range(n)] for j in range(n)]

