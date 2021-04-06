
def split_n_cases(txt, cases):
  n, check = divmod(len(txt), cases)
  if check:
    return ['Error']
  return [txt[i:i+n] for i in range(0, len(txt), n)]

