
def calculate_arrowhead(lst):
  left = sum([len(el) for el in lst if el[0] == '>'])
  right = sum([len(el) for el in lst if el[0] == '<'])
  if left == right:
    return ''
  elif left > right:
    return (left - right) * '>'
  else:
    return (right - left) * '<'

