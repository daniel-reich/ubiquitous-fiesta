
def repetition(txt, n):
  return '' if not n else txt + repetition(txt, n-1)

