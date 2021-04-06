
def caesar_cipher(s, k):
  alpha = "abcdefghijklmnopqrstuvwxyz"
  length = 25
  cypher = ""
  yup = False
  
  
  for ch in s:
    if(not ch.isalpha()):
      cypher += ch
      continue
      
    if(ch.isupper()):
      yup = True
    
    current_index = alpha.find(ch.lower())
    
    for i in range(k,0,-1):
      if(current_index == 25):
        current_index = 0
      else:
        current_index += 1
    new_index = current_index
    
    nxt = alpha[new_index]
    if(yup):
      cypher += nxt.upper()
      yup = False
    else:
      cypher += nxt
  return cypher

