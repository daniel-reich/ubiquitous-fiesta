
def remix(txt, lst):
  return ''.join(w for w in [txt[lst.index(i)] for i in range(len(lst))])

