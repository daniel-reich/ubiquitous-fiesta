
def multiply_by_11(s, r=None):
  return multiply_by_11(s, [int(s[-1])]) if not r else ''.join(map(str, r)) if not len(s) else \
    multiply_by_11(s[:-1], [int(('0'+s)[-2:-1])+int(('0'+s)[-1])+int(r[0] > 9), r[0] % 10]+r[1:])

