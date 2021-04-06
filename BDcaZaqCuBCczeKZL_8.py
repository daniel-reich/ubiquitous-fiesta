
def arrow(num):
  if num % 2 == 0:
    return [x * '>' for x in range(1,num + 1)] + [x * '>' for x in range(num, 0, -1)]
  return [x * '>' for x in range(1,num + 1)] + [x * '>' for x in range(num-1, 0, -1)]

