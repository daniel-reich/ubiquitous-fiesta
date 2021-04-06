
def censor(s):
  return " ".join(list(map(lambda x: "*"*len(x) if len(x) > 4 else x, s.split())))

