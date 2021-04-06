
def remix(txt, lst):
  return ''.join(x[1] for x in sorted(zip(lst, txt)))

