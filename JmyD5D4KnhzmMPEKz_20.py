
def constraint(txt):
  txt = txt.casefold()
  lst_ch = [ch for ch in txt
                if ch.isalpha()]
  set_ch = set(lst_ch)
  
  if len(set_ch) == 26: 
    return 'Pangram'
  if len(lst_ch) == len(set_ch):
    return 'Heterogram'
    
  words = txt.split(' ')
  first_ch = set(word[0] 
                for word in words)
  if len(first_ch) == 1:
    return 'Tautogram'
    
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  share_ch = [ch for ch in alphabet
             if all(ch in word
                 for word in words)]
  if len(share_ch) != 0:
    return 'Transgram'
    
  return 'Sentence'

