
def reverse(txt):
  if len(txt) == 0:
    return txt
    
  else:
    
    first_letter = txt[0]
    
    return reverse(txt[1:]) + first_letter

