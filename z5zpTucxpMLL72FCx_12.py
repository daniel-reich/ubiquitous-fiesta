
def grab_city(txt):
  txt = txt[::-1]
  start = txt.index(']')
  end = txt.index('[')
  return txt[end - 1:start:-1]

