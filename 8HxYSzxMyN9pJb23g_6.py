
def split_n_cases(inp, cases):
  if len(inp)%cases:
    return ["Error"]
  return [inp[i:i+len(inp)//cases] for i in range(0,len(inp), len(inp)//cases)]

