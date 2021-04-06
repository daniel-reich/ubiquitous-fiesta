
def first_repeat(chars):
  try:
    return [i for i in chars if chars.count(i) > 1][0]
  except:
    return '-1'

