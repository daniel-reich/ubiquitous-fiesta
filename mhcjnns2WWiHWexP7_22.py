
def calculate_arrowhead(lst):
  x = eval(''.join(lst).replace('<', '-1').replace('>', '+1'))
  return (-x)*'<' if x < 0 else x*'>'

