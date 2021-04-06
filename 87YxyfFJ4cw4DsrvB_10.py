
def generate_rug(n):
  if n == 1:
    return [[0]]
  else:
    result = []
    a = n // 2
    for i in range(n):
      temp = []
      for j in range(n):
        b = abs(a-i)
        c = abs(a-j)
        if b > c:
          d = b
        else:
          d = c
        temp.append(d)
      result.append(temp)
    return result

