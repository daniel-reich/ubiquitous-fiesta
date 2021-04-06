
def split_n_cases(txt, cases):
  sk = int(len(txt)/cases) if len(txt)%cases==0 else "Error"
  return [sk] if sk=="Error" else [txt[i:i+sk] for i in range(len(txt))[::sk]]

