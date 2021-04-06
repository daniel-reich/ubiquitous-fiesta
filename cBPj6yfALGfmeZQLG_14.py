
def vertical_txt(txt):
  l = txt.split( " " )
  m = max( [ len( s ) for s in l ] )
  l = [ x + ( m - len( x ) ) * " " for x in l ]
  r = [ [ ] for i in range(m) ]
  for i in range( m ) :
    for x in l :
      r[ i ].append( x[ i ] )
  return r

