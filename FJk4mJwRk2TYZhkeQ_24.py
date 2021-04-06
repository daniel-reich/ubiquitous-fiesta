
def accum(txt):
  return '-'.join(txt[n].upper() + txt[n].lower()*(n) for n in range(len(txt)))

