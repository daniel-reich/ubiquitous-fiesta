
def flash(f):
  try:
    return round(eval(''.join(str(x) for x in f).replace('x','*')),2)
  except:
    return None

