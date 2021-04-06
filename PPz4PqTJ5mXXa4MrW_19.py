
def ulam(n):
  seq = [1,2]
  s = set([1,2])
  for i in range(3,6783):
    count = 0
    for x in range(len(seq)):
      if (i-seq[x]) in s and seq[x] != (i-seq[x]):
        count += 1
      if count > 2:
        break
    if count == 2:
      seq.append(i)
      s.add(i)
  return seq[n-1]

