
def organize(txt):
  if txt:
    return {k: int(v) if v.isnumeric() else v
         for k, v in zip(("name", "age", "occupation"), txt.split(", "))}
  return {}

