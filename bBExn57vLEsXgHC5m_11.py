
def same_line(lst):
  a, b, c = lst
  if (a[0]==b[0]==c[0]) or (a[1]==b[1]==c[1]): return True
  else:
    try: 
      if (b[1]-a[1])/(b[0]-a[0])==(c[1]-a[1])/(c[0]-a[0]): return True
    except: pass
  return False

