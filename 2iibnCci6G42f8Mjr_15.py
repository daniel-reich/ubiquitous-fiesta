
def guess_score(code, guess):
  black = 0
  white = 0
  for i in range(len(code)):
    code_ = code.replace(code[i], '')
    if guess[i] == code[i]:
      black+=1
    elif guess[i] in code_:
      white += 1
  overlap = len(code) - len(set(guess))
  white -= overlap
  return {'black':black, 'white':abs(white)}

