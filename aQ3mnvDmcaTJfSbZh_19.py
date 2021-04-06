
def bw_transform(text):
  l = len(text)
  rotations = ["".join(text[(i+j)%l] for i in range(l)) for j in range(l)]
  return "".join(w[-1] for w in sorted(rotations))

