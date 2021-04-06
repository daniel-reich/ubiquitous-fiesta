
def find_broken_keys(txt1, txt2):
  res = []
  for k in range(0, len(txt1)):
    if txt1[k] != txt2[k] and txt1[k] not in res:
      res.append(txt1[k])
  return res

