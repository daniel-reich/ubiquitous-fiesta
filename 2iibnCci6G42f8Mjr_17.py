
def guess_score(code, guess):
  code, guess = list(code), list(guess)
  b, w = 0, 0
  for i in range(len(code)):
    if guess[i] == code[i]:
      b += 1
      guess[i], code[i] = '*', '*'
​
  for i in guess:
    if i in code and i != '*':
      w += 1
      code[code.index(i)] = '*'
  
  return {"black": b, "white": w}

