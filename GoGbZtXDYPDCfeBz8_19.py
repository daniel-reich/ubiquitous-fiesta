
def magic(txt):
  l=txt.split()
  mm=int(l[0])
  dd=int(l[1])
  y=l[2]
  return mm*dd==int(y[-1]) or mm*dd==int(y[-2:]) or mm*dd==int(y[-2:] )

