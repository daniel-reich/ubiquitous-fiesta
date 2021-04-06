
def emotify(txt):
  switch = {
    'smile':':D', 'grin':':)', 'sad':':(', 'mad':':P',
  }
  return txt[:8] + switch[txt[8:]]

