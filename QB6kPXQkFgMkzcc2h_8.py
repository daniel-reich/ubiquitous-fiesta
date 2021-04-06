
def remove_abc(txt):
  if all([not i in txt for i in "abc"]):
    return None
  else: 
    return "".join([i if not i in "abc" else "" for i in txt ])

