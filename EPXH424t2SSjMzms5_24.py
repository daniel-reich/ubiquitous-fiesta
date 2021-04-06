
def remix(s, lst):
  return ''.join(s[i] for i, _ in sorted(enumerate(lst), key=lambda k: k[1]))

