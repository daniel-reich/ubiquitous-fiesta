
def organize(txt):
  return {} if not txt else {"name": txt.split(",")[0], "age": int(txt.split(",")[1]), "occupation": txt.split(",")[-1][1:]}

