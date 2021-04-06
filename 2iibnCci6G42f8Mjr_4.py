
def guess_score(code, guess):
  black = 0
  white = 0
  for c, g in zip(code, guess):
    if c == g: black += 1
    elif c in guess: white += 1
  return {'black': black, 'white': white}

