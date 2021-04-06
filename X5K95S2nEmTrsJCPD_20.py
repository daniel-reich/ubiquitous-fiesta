
def emotify(txt):
  e={'smile':":D",'grin':':)','sad':':(','mad':':P'}
  return ' '.join(e[x] if x in e.keys() else x for x in txt.split())

