
def split_n_cases(txt, cases):
  if len(txt) % cases != 0:
    return ['Error']
  output = []
  slice = len(txt)//cases
  while len(txt)> 0:
    output.append(txt[:slice])
    txt = txt[slice:]
  return output

