
def bw_transform(text):
  bwm = []
  for i in range(len(text)):
    text = text[1:] + text[:1]
    bwm.append(text)
  bwm = sorted(bwm)
  return "".join(bwm[i][-1] for i in range(len(bwm)))

