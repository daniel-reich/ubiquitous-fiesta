
def rotated_words(txt):
  nc = "WMHINOSXZ" 
  
  return sum(1 for i in set(txt.split()) if all(char in nc for char in i))

