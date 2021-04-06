
def calculate_arrowhead(lst):
  total = sum((-1, 1)[i == '>'] for i in ''.join(lst))
  return '>' * total if total > 0 else '<' * abs(total)

