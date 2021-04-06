
def calculate_arrowhead(lst):
  arrows = sum([-arrow.count('<') + arrow.count('>') for arrow in lst])
  return ['<' * abs(arrows), '>' * arrows][arrows > 0]

