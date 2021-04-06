
def multiply_by_11(n):
  lst = [int(x) + int(y) for x, y in zip(n, n[1:])]
  lst = [int(n[0])] + lst + [int(n[-1])]
  for x in range(len(lst)-2, 0, -1):
    if lst[x] > 9:
      lst[x] -= 10
      lst[x-1] += 1
  return ''.join(str(x) for x in lst)

