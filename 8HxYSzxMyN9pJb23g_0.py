
def split_n_cases(txt, n):
  l = len(txt) // n
  return ["Error"] if len(txt) % n else [txt[x*l:x*l+l] for x in range(n)]

