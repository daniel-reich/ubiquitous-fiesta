
def accum(txt):
  return '-'.join([char.upper()+char.lower()*index for index,char in enumerate(txt)])

