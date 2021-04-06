
def maurice_wins(m, s):
  m[0],m[1],m[2] = m[1],m[2],m[0]
  return 2==sum(m>s for m,s in zip(m,s))

