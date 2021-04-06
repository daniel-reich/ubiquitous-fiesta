
def monkey_talk(txt):
  vowel='aeiou'
  txt=txt.lower()
  A=txt.split()
  B=[]
  for x in A:
    if x[0] in vowel:
      B.append('eek')
    else:
      B.append('ook')
  return ' '.join(B).capitalize()+'.'

