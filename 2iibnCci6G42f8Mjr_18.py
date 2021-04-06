
def guess_score(code, guess):
  blk = [1 if code[i] == guess[i] else 0 for i in range(len(code))]
  remguess = [guess[i] for i in range(len(code)) if code[i] != guess[i]]
  remcode = [code[i] for i in range(len(code)) if code[i] != guess[i]]
  uniques = list(set(remguess))
  wht = [min(remguess.count(i), remcode.count(i)) for i in uniques]
  
  
  outdict = {}
  outdict["black"] = sum(blk)
  outdict["white"] = sum (wht)
  return outdict

