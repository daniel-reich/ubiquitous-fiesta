
def shift_sentence(txt):
  first, rest = [i[0] for i in txt.split()], [i[1:] for i in txt.split()]
  return ' '.join(first[i-1]+rest[i] for i in range(len(first)))

