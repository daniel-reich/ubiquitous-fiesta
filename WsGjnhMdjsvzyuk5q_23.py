
def dashed(txt):
  vol="aouie"
  new=""
  for i in range(len(txt)):
    if txt[i].lower() in vol:
      new+="-{}-".format(txt[i])
    else:
      new+=txt[i]
  return new

