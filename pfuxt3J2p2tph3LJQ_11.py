
def forbidden_letter(char, lst):
  for word in lst:
    for letter in word:
      if char == letter:
        return False
        
  return True

