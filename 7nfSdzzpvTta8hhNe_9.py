
def organize(txt):
  if not txt: return {}
  n, a, o = txt.split(", ")
  return {"name": n, "age": int(a), "occupation": o}

