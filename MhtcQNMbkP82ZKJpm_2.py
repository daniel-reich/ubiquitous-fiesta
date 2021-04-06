
def get_notes_distribution(students):
  n = [y for x in students for y in x['notes'] if y in range(1,6)]
  l = [(x, n.count(x)) for x in set(n)]
  return dict(l)

