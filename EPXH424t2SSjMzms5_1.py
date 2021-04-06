
def remix(txt, lst):
  return ''.join(b for a, b in sorted(zip(lst, txt)))

