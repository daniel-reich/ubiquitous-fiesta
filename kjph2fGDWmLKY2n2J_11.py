
import re
def valid_color(color):
  p = re.compile('rgb(|a)\(((\d|\.|\%|\s)*,){2,3}(\d|\.|\%|\s)*\)')
  if not re.match(p, color):
    return False
  is_rgba = 'a' in color
  values = color[(5 if is_rgba else 4):-1].split(',')
  if is_rgba and len(values) == 4:
    rgb = values[:3]
    if not 0 <= float(values[3]) <= 1:
      return False
  elif not is_rgba and len(values) == 3:
    rgb = values
  else:
    return False
  try:
    rgb = [float(v) if '%' not in v else float(v.replace('%', ''))*2.55 for v in rgb]
  except:
    return False
  return all(0 <= v <= 255 for v in rgb)

