
def censor(s):
  return ' '.join('*' * len(x) if len(x) > 4 else x for x in s.split())

