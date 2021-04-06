
def bw_transform(text):
  return "".join([x[-1] for x in sorted([text[i:] + text[:i] for i in range(len(text))])])

