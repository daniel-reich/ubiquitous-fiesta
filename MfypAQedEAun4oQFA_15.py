
def perrin(n):
  per, i = [3,0,2], 3
  while len(per) <= n:
    per.append(per[i-3] + per[i-2])
    i += 1
  return per[n]

