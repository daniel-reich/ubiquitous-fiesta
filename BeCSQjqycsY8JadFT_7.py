
def recur_index(txt, itms=None, idx=0):
  if idx == 0:
    itms = {}
    txt = iter(txt if txt else "")
  try:
    nItm = next(txt)
    if nItm in itms:
      return {nItm:[itms[nItm], idx]}
    else:
      itms[nItm] = idx
      return recur_index(txt, itms, idx + 1)
  except StopIteration:
    return {}

