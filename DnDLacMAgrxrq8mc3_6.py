
def blah_blah(txt, n):
  if len(txt.split()) <= n:
    return ((len(txt.split()) * ' blah') + '...').strip()
  else:
    return ' '.join(txt.split()[:-n]) + (n * ' blah') + '...'

