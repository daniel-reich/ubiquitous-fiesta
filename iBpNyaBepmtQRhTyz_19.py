
def c_cipher(msg, keyword):
  a = 'abcdefghijklmnopqrstuvwxyz0123456789'
  if ' ' in msg:
    msg= msg.lower()
    msg = [c for c in msg if c in a]
    l1, l2 = len(msg), len(keyword)
    pad = l2 - l1 % l2 if l1 % l2 else 0
    msg = msg + ['x'] * pad
    msg = [msg[i*l2:i*l2+l2] for i in range(len(msg) // l2)]
    k = [e for e,c in sorted(enumerate(keyword), key=lambda x: x[1])]
    return ''.join(g[i] for i in k for g in msg)
  else:
    l1, l2 = len(msg), len(keyword)
    h = l1 // l2
    k = [e for e,c in sorted(enumerate(keyword), key=lambda x: x[1])]
    msg = [msg[i*h:i*h+h] for i in range(l2)]
    msg = sorted(zip(msg, k), key=lambda x: x[1])
    return ''.join([g[0][i] for i in range(h) for g in msg])

