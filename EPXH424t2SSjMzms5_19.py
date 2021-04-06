
def remix(txt, lst):
  a = sorted(zip(lst, txt))
  return "".join(ch for (i, ch) in a)

