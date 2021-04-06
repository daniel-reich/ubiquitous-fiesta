
def remix(txt, lst):
  return ''.join(x for _,x in sorted(zip(lst,txt)))

