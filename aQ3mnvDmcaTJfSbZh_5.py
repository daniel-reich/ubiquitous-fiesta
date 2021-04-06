
def bw_transform(text):
  rotated=[text[i:] + text[:i] for i in range(len(text))]
  rotated.sort()
  return "".join([el[-1] for el in rotated])

