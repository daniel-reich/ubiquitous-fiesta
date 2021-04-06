
def most_frequent_char(l):
  l = ''.join(l)
  s = sorted(set(l))
  c = [l.count(i) for i in s]
  return [a for a,b in zip(s,c) if b==max(c)]

