
def junction_or_self(n):
  retArr = []
  for num in range(1,n+1):
    if n == num + sum([int(i) for i in str(num)]):
      retArr.append(num)
  return sorted(retArr,reverse=True) if retArr else "Self"

