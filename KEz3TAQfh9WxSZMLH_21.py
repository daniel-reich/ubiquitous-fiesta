
def count_all(txt):
  digits, alphas = 0, 0 
  digits = sum([digits + 1 for ch in range(len(txt)) if txt[ch].isdigit()])
  alphas = sum([alphas + 1 for ch in range(len(txt)) if txt[ch].isalpha()])
  return {"LETTERS" : alphas, "DIGITS" : digits}

