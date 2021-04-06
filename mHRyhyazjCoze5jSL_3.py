
def double_swap(txt, c1, c2):
  return "".join(c1 if i == c2 else c2 if i == c1 else i for i in txt)

