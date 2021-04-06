
def bird_code(lst):
  def name(i):
    j = ''
    for w in i:
      if w == '-':
        j = j + ' '
      else:
        j = j + w
    j = j.split(" ")
    if len(j) == 1:
      return ''.join(j[0][:4]).upper()
    elif len(j) == 2:
      return ''.join((j[0][:2] + j[1][:2])).upper()
    elif len(j) == 3:
      return ''.join((j[0][:1] + j[1][:1] + j[2][:2])).upper()
    else:
      return ''.join([k[0] for k in j]).upper()
  return [name(i) for i in lst]

