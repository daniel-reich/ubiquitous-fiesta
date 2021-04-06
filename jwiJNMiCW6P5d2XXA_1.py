
def does_rhyme(txt1, txt2):
  return [i for i in txt1.lower().split()[-1] if i in 'aeiou']==[i for i in txt2.lower().split()[-1] if i in 'aeiou']

