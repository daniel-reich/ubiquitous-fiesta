
def binary_clock(time):
  digs = list(map(int, time.replace(':', '')))
  h1 = '  {:02b}'.format(digs[0])
  h2 = '{:04b}'.format(digs[1])
  m1 = ' {:03b}'.format(digs[2])
  m2 = '{:04b}'.format(digs[3])
  s1 = ' {:03b}'.format(digs[4])
  s2 = '{:04b}'.format(digs[5])
  return [''.join(i) for i in zip(h1,h2,m1,m2,s1,s2)]

