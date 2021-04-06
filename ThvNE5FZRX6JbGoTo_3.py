
def inverter(txt, ty):
  t = txt.split()
  s = ' '.join([t[-1].capitalize()]+ [x.lower() for x in t[:-1]][::-1]) 
  r = ' '.join([t[0][::-1].capitalize()]+ [x.lower()[::-1] for x in t[1:]])
  return s if ty == "P" else r

