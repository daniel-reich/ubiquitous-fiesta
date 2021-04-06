
def is_kaprekar(n):
  if n<4: return n==1
  else: return n==int(str(n*n)[:len(str(n*n))//2])+int(str(n*n)[len(str(n*n))//2:])

