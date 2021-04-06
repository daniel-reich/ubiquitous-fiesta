
def divisible_by_left(n):
  a = [int(i) for i in str(n)][::-1]
  return (([a[i]%a[i+1] == 0 if a[i+1] != 0 else 
          False for i in range(len(a)-1)]+[False])[::-1])

