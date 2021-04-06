
def number_of_repeats(s):
  A=[x for x in range(1, len(s)+1) if len(s)%x==0]
  B=dict([(x, y) for x in A for y in A if x*y==len(s)])
  for x in A:
    if s[:x]*B[x]==s:
      return B[x]

