
def paul_cipher(txt):
  
  a = 'abcdefghijklmnopqrstuvwxyz'.upper()
  a_to_pos = {}
  pos_to_a = {}
  
  for n in range(26):
    a_to_pos[a[n]] = n+1
    pos_to_a[n + 1] = a[n]
  
  txt = txt.upper()
  
  movement = None
  encoded = ''
  
  for l8r in txt:
    if movement == None or l8r not in a:
      encoded += l8r  
    else:
      try:
        encoded += pos_to_a[a_to_pos[l8r] + movement]
      except KeyError:
        encoded += pos_to_a[a_to_pos[l8r] + movement - 26]
    try:
      movement = a_to_pos[l8r]
    except KeyError:
      continue
  
  return encoded

