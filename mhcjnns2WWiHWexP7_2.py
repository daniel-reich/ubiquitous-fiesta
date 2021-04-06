
def calculate_arrowhead(lst):
  string = ''.join(i for i in lst)
  left = string.count('<')
  right = string.count('>')
  return (right - left) * '>' if right > left else (left - right) * '<'

