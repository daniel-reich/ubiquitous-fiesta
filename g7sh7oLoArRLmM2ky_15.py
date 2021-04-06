
from itertools import chain, repeat
def baconify(msg, mask=None):
  a = 'abcdefghijklmnopqrstuvwxyz'
  d = {c:e for e,c in enumerate(a)}
  d['.'], d[' '] = 30, 31
  if mask:
    msg = ''.join(format(d[ch], '05b') for ch in msg.lower() if ch in d)
    msg = chain(iter(msg), repeat('1'))
    mask = mask.lower()
    return ''.join(ch if ch not in a else ch if next(msg)=='1' else ch.upper() for ch in mask)
  else:
    d = {v:k for k,v in d.items()}
    msg = [c for c in msg if c.lower() in a]
    msg = [msg[i:i+5] for i in range(0, len(msg), 5)]
    if len(msg[-1]) < 5: msg.pop()
    return ''.join(d[int(''.join('1' if ch.islower() else '0' for ch in grp), 2)] for grp in msg)

