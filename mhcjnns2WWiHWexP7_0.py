
def calculate_arrowhead(lst):
  diff = sum([-1, 1][i == '>'] for i in ''.join(lst))
  return ['>', '<'][diff < 0] * abs(diff)

