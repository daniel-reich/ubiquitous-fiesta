
def valid(txt):
  return len(txt) in [4, 6] and len(txt) == len([i for i in txt if i in '0123456789'])

