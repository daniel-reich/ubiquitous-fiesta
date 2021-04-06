
def divisibility_rule(n):
  rep = [1, 10, 9, 12, 3, 4]
  seq = []
  while True:
    n = sum(int(x) * rep[i % 6] for i, x in enumerate(str(n)[::-1]))
    if n not in seq:
      seq.append(n)
    else:
      break
  return n

