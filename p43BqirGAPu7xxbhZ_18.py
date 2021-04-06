
def diamond(n):
  if n%2==0:
    return [[[1 if k==n/2+i or k==n/2-i-1 or k==i-n/2+1 or k==n/2+(n-2-i) else 0 for k in range(abs(n))] for i in range(abs(n-1))], 'good cut']
  else:
    return [[[1 if k==n//2+i or k==n//2-i or k==i-n//2 or k==n//2+(n-1-i) and i>n//2 else 0 for k in range(n)] for i in range(n)], 'perfect cut']

