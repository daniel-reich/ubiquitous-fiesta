
def meme_sum(a, b):
  a,b = str(a),str(b)
  lg = max(len(a),len(b))
  a,b = a.zfill(lg),b.zfill(lg)
  return int(''.join(str(int(x)+int(y)) for x,y in zip(a,b)))

