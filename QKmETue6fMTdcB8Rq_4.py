
def repetition(txt, n, c = 0):
  if c<n:
    return txt * n
    repetition(txt, n, c = c + 1)

