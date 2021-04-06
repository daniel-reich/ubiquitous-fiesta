
def emotify(txt):
  dic = {'smile': ':D', 'grin': ':)', 'sad': ':(', 'mad':':P'}
  for i in dic:
    txt = txt.replace(i, dic[i])
  return txt

