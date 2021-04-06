
def get_lucky_number(size, nth):
  l = [i for i in range(1,size+1,2)]
  i = 1
  def sieve(seq, p):
    ex = [seq[i] for i in range(p-1,len(seq),p)]
    return sorted(list(set(seq) - set(ex)))
  while len(l) >= l[i]:
    l = sieve(l, l[i])
    i += 1
  return (l[nth-1])

