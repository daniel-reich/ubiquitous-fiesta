
def full_key_name(piece):
  
  info = piece.split(' in ')[1]
  
  if info.isupper() == True:
    return piece + ' major'
  elif info[0].isupper() == True:
    return piece + ' major'
  else:
    words = piece.split()
    info = info.capitalize()
    
    tr = ' '.join(words[:-1])
    
    tr += ' ' + info
    tr += ' minor'
    
    return tr

