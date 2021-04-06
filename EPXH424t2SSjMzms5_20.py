
def remix(txt, lst):
  return "".join([ txt[lst.index(x)] for x in range(len(txt)) ])

