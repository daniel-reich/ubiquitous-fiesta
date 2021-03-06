
def valid_color (color):
  def check(x):
    if isinstance(x, int): return 0<=x<=255
    else: return 0<=x<=1
  def rgb(r,g,b): return check(r) and check(g) and check(b)
  def rgba(r,g,b,a): return rgb(r,g,b) and 0<=a<=1
  if ' (' in color: return False
  try: return eval(color.replace('%', '*0.01'), {'rgb': rgb, 'rgba': rgba}, {})
  except: return False

