
def guess_score(code, guess):
  b, w = 0, 0
  for x, y in zip(code, guess):
    if x == y:
      b += 1
    elif x in guess:
      w += 1
  return {'black': b, 'white': w}

