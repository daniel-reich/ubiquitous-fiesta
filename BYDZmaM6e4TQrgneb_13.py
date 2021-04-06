
def fib_fast(num):
  flist = [0, 1]
  any(map(lambda x: flist.append(sum(flist[-2:])), range(2, num)))
  return sum(flist[-2:])

