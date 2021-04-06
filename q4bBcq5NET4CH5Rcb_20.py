
def jay_and_bob(txt):
  d = {'half':2,'quarter':4,'eighth':8,'sixteenth':16}
  return str(int(28/d[txt]))+' grams' if str(28/d[txt])[-1] == '0' else str(round(28/d[txt],2))+' grams'

