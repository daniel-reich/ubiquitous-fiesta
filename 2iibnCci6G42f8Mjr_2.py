
from collections import Counter
def guess_score(code, guess):
  code, guess = [int(c) for c in code], [int(g) for g in guess]
  blacks = [i for i in range(len(code)) if code[i] == guess[i]]
  code, guess = [c for i, c in enumerate(code) if i not in blacks], [g for i, g in enumerate(guess) if i not in blacks]
  cc, cg = Counter(code), Counter(guess)
  whites = sum(min(cc[k], cg.get(k, 0)) for k in cc.keys())
  return {'black': len(blacks), 'white': whites}

