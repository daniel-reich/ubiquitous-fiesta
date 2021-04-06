
def bw_transform(text):
  a = [text[i+1:]+text[:i+1] for i in range(len(text))]
  return"".join(i[-1] for i in sorted(a))

