
def loves_me(n):
  ans = ["Loves me" if i%2!=0 else "Loves me not" for i in range(1,n+1)]
  ans[-1] = ans[-1].upper()
  return ", ".join(i for i in ans)

