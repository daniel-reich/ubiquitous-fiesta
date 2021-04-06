
def split_n_cases(txt, cases):
  if len(txt)%cases: return ["Error"]
  res, sl = [], len(txt) // cases
  for i in range(0, len(txt), sl):
    res.append(txt[i:i+sl])
  return res

