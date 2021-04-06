
def double_char(txt):
    res = ''
    
    for letter in txt:
      letter = letter + letter
      res += letter
    return res

