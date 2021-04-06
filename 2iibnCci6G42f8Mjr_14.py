
def guess_score(code, guess):
  a = sum([1 for i in code if i in guess])
  b = sum([1 for i in range(len(code)) if code[i]==guess[i]])
  return {"black":b , "white":a-b}

