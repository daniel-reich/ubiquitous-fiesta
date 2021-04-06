
def organize(txt):
  if txt:
    n,a,o,*z = txt.split(",")
    return {"name":n, "age":int(a.strip()), "occupation":o.strip()}
  return {}

