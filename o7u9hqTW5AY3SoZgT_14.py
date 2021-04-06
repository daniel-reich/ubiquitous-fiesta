
import re
def switcheroo(txt):
  print( txt)
  switch_1 = re.sub( r'\Bnts\b', '!!!', txt )
  switch_2 = re.sub( r'\Bnce\b', '???', switch_1 )
  final = switch_2.replace('!!!', 'nce').replace('???','nts')
  return( final)

