
def bw_transform(t):
  return "".join(w[-1] for w in sorted(t[i:]+t[:i] for i in range(len(t))))

