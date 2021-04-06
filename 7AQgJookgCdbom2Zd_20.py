
def pig_latin(txt):
  return ' '.join([i[1:]+i[0]+'ay' if i.lower()[0] not in 'aeiou' else i+'way' for i in txt[:-1].split()]).capitalize()+txt[-1]

