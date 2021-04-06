
def color_conversion(h):
  if type(h) == str:
    h = h.replace('#','')
    if len(h) != 6:
      return "Invalid input!"
    r,g,b = h[:2],h[2:4],h[4:]
    try:
      return {'r':int(r,16),'g':int(g,16),'b':int(b,16)}
    except:
      return "Invalid input!"
  else:
    r,g,b = h['r'],h['g'],h['b']
    if any(x>255 or x < 0 for x in (r,g,b)):
      return "Invalid input!"
    return '#{}{}{}'.format(hex(r)[-2:],hex(g)[-2:],hex(b)[-2:]).replace('x','0')

