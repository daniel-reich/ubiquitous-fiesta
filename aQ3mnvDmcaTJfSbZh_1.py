
def bw_transform(text):
  return "".join(t[-1] for t in sorted(text[i:]+text[:i] for i in range(len(text))))

