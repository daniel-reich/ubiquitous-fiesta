
def calculate_arrowhead(lst):
  s = sum(-1 if i == '<' else 1 for i in ''.join(lst))
  if s < 0:
    return '<'*abs(s)
  else:
    return '>'*s

