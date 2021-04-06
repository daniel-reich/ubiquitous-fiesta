
def emotify(txt):
  txt = txt.split()
  D = {
  'smile': ':D',
  'grin': ':)',
  'sad': ':(',
  'mad': ':P',
  }
  for i, char in enumerate(txt):
    if char in D.keys():
      txt[i] = D[char]
  return ' '.join(txt)

