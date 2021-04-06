
def check_title(txt):
  words = txt.split() 
  return all([word[0].isupper() for word in words])

