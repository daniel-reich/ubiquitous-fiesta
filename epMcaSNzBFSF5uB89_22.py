
def currently_winning(s):
  y, o = s[:-1:2], s[1::2]
  return ['Y' if sum(y[:i]) > sum(o[:i]) else 'O' if sum(o[:i]) > sum(y[:i]) else 'T' for i in range(1, len(y)+1)]

