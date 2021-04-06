
def accum(txt):
  return '-'.join([txt[i].capitalize()+txt[i].lower()*i for i in range(len(txt))])

