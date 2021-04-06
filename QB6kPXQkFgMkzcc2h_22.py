
letters = "abc"
def remove_abc(txt):
  a = "".join([i for i in txt if i not in letters])
  return None if len(a)  == len(txt) else a

