
def bw_transform(text):
  BWT = [(text[i:] + text[:i]) for i in range(len(text))]
  return ''.join(i[-1] for i in sorted(BWT))

