
def emotify(txt):
  sub = {'smile': ':D', 'grin': ':)', 'sad': ':(', 'mad': ':P'}
  return txt[:8] + sub[txt[8:]]

