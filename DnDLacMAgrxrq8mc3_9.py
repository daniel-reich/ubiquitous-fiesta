
def blah_blah(txt, n):
  l = len(txt.split(' '))
  return ' '.join(txt.split(' ')[0:l-n])+' blah'*(n-1)+' blah...' if n<l else 'blah'+' blah'*(l-2)+' blah...'

