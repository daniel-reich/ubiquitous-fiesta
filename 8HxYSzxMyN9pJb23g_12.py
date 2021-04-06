
def split_n_cases(txt, cases):
  try:
    if len(txt) % cases > 0:
      return ["Error"]
    parts = len(txt) / cases
    return list(map(lambda x: txt[x:x+int(parts)],range(0,len(txt),int(parts))))
  except ValueError:
    return ["Error"]

