
def split_n_cases(txt, cases):
  if len(txt)%cases==0:
    n=int(len(txt)/cases)
    return [txt[i:i+n] for i in range(0,len(txt), n)]
  else:
    return [ "Error" ]

