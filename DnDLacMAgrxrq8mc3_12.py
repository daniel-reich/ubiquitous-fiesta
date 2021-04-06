
def blah_blah(txt, n):
  r=txt.split(' ')
  for i in range((len(r)-n),len(r),1):
    r[i]='blah'
  return ' '.join(r)+'...'

