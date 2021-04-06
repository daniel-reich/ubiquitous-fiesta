
def alpha_range(start, stop, step=1):
  upper_letters = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  lower_letters = ' abcdefghijklmnopqrstuvwxyz'
  if step > -26 and step < 26 and step != 0:
    if start.isupper() and stop.isupper():
      a, b = ord(start) - 64, ord(stop) - 64
      if step > 0:
        a, b = min([a, b]), max([a, b]) + 1
      else:
        a, b = max([a, b]), min([a, b]) - 1
      return list(upper_letters[a:b:step])
    elif start.islower() and stop.islower():
      a, b = ord(start) - 96, ord(stop) - 96
      if step > 0:
        a, b = min([a, b]), max([a, b]) + 1
      else:
        a, b = max([a, b]), min([a, b]) - 1
      return list(lower_letters[a:b:step])
    else:
      return 'both start and stop must share the same case'
  else:
    return 'step must be a non-zero value between -26 and 26, exclusive'

