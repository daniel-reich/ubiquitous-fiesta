
def split_n_cases(txt, cases):
  return [ "Error" ] if (len(txt)%cases) else [txt[i:i+len(txt)//cases] for i in range(0, len(txt),len(txt)//cases ) ]

