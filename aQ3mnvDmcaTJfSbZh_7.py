
def bw_transform(txt):
  return ''.join(i[-1] for i in sorted(txt[i:]+txt[:i] for i in range(len(txt))))

