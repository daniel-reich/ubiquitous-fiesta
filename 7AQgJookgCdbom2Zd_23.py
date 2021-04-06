
def pig_latin(txt):
  return (' '.join([i+'way' if i[0].lower() in 'aeuio' else i[1:]+i[0]+'ay' for i in txt[:-1].split()])+txt[-1]).capitalize()

