
def emotify(txt):
  d = {'smile': ':D', 'grin': ':)', 'sad': ':(', 'mad': ':P'}
  return txt.replace(txt.split()[-1], d[txt.split()[-1]])

