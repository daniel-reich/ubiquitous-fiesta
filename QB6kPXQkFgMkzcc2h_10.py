
def remove_abc(txt):
  return "".join([i for i in txt if i not in 'abc']) if len([i for i in txt if i in 'abc']) >= 1 else None

