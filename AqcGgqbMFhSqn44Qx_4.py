
def tweet(txt):
  res = []
  t = txt.split()
  for k in range(0, len(t)):
    if t[k].startswith("#") or t[k].startswith("@"):
      res.append(t[k].strip(".").strip(",").strip("?").strip("!"))
  return " ".join(res)

