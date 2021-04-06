
def gimme_the_letters(spectrum):
  a,b = [ ord(i) for i in spectrum.split('-') ]
  return ''.join( [ chr(i) for i in range( a,b+1 ) ] )

