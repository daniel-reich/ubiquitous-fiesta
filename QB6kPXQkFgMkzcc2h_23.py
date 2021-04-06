
def remove_abc(txt):
  res = "";
  for i in txt:
    if i in "abc":
      res += "";
    else:
      res += i;
  return None if len(res)==len(txt) else res;

