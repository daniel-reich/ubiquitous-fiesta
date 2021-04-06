
def silence_Trump(txt):
  return "".join([x for x in txt if x not in "aeiouAEIOU"])

