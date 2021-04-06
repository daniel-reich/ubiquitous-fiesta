
def guess_score(code, guess):
  blacks = sum(c == g for c, g in zip(code, guess))
  whites = sum(c in guess for c in code) - blacks
  return {'black': blacks, 'white': whites}

