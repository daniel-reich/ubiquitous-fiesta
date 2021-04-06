
def repetition(txt, n):
  return '' if n <= 0 else txt + repetition(txt, n - 1)

