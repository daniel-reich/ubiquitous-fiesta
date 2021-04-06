
def bw_transform(text):
  return ''.join(list(zip(*sorted(text[n:]+text[:n] for n in range(len(text)))))[-1])

