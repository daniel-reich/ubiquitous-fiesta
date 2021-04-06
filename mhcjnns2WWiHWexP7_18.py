
def calculate_arrowhead(lst):
  string = ''.join(lst)
  sx = string.count('<')
  dx = string.count('>')
  return '<'*(sx-dx) if sx > dx else '>'*(dx-sx) if dx > sx else ''

