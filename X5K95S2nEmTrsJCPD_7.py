
def emotify(txt):
  dic = {'smile':':D',
  'grin':':)',
  'sad': ':(',
  'mad':':P'}
  x = txt.split(' ')
  return ' '.join(['Make me',dic[x[2]]])

