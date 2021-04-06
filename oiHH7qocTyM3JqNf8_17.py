
def move(word):
  new_word = ""
  
  for ch in word:
    if ch == 'Z':
      ch = 'A'
    elif ch == 'z':
      ch = 'a'
    else:
      ch = chr(ord(ch) + 1)
      
    new_word += ch
      
  return new_word;

