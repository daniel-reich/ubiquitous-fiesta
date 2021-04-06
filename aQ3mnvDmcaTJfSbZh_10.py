
def bw_transform(text):
  return "".join(s[-1] for s in sorted(text[i:] + text[:i] for i in range(len(text))))

