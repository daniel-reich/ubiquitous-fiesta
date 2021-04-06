
def can_exit(lst):
  width = len( lst[ 0 ] )
  heigth = len( lst )
  paths = [ [ [ 0, 0 ] ] ]
  while True :
    new_paths = [ ]
    for p in paths :
      x, y = p[ -1 ][ 0 ], p[ -1 ][ 1 ]
      if lst[ max( 0, y - 1 ) ][ x ] == 0 and [ x, max( 0, y - 1 ) ] not in p :
        new_paths.append( p + [ [ x, max( 0, y - 1 ) ] ] )
      if lst[ y ][ min( width - 1, x + 1 ) ] == 0 and [ min( width - 1, x + 1 ), y ] not in p :
        new_paths.append( p + [ [ min( width - 1, x + 1 ), y ] ] )
      if lst[ min( heigth - 1, y + 1 ) ][ x ] == 0 and [ x, min( heigth - 1, y + 1 ) ] not in p :
        new_paths.append( p + [ [ x, min( heigth - 1, y + 1 ) ] ] )
      if lst[ y ][ max( 0, x - 1 ) ] == 0 and [ max( 0, x - 1 ), y ] not in p :
        new_paths.append( p + [ [ max( 0, x - 1 ), y ] ] )
    if len( new_paths ) == 0 :
      return False
    for p in new_paths :
      if [ width - 1, heigth - 1 ] in p :
        return True
    paths = new_paths

