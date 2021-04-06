
def sort_by_last(txt):
  txt = txt.split()
  txt.sort(key = lambda x:x[-1])
  return ' '.join(txt)

