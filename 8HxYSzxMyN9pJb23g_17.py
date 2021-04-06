
def split_n_cases(txt, cases):
  if len(txt)%cases == 0:
    divisor = len(txt)//cases
    splitted = []
    
    for n in range(0, len(txt), divisor):
      splitted.append(txt[n:n+divisor])
    
    return splitted
  else:
    return ['Error']

