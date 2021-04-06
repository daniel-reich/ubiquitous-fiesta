
def count_same_ends(txt):
  txt = ''.join(i for i in txt if i.isalpha() or i == ' ').lower()
  return sum(i[0] == i[-1] and len(i) > 1 for i in txt.split())

