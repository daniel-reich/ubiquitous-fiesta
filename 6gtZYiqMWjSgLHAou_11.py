
def format_num(n):
  ns = str(n)
  for i in [3, 7, 11]:
    if len(ns) > i:
      ns = ns[:-i]+','+ns[-i:]
  return ns

