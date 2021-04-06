
def markdown(c):
  return lambda s,w,x=c: \
         ' '.join(x+k+x if w.lower() in k.lower() else k for k in s.split())

