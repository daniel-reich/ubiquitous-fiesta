
def count_lone_ones(n):
  p = [int(i) for i in list(str(n))]
  o = [0]+p+[0]
  return len([o[i] for i in range(len(o)) if o[i] == 1 and o[i-1] != 1 and o[i+1] != 1])

