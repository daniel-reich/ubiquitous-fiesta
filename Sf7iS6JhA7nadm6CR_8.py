
def divisibility_rule(n):
  seq = [1, 10, 9, 12, 3, 4]
  cur = n
  prev = 0
  while cur!=prev:
    prev = cur
    cur = 0
    for i in range(len(str(prev))):
      cur+=int(str(prev)[len(str(prev))-i-1])*seq[i%6]
  return cur

