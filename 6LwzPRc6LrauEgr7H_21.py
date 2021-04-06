
def worm_length(worm):
  l=worm.count('-')
  return str(l*10)+' mm.' if l==len(worm) and l>0 else 'invalid'

