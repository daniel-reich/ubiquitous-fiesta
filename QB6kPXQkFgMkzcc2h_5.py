
def remove_abc(txt):
  return None if all(x not in 'abc' for x in txt) else txt.replace('a','').replace('b','').replace('c','')

