
def letters_only(txt):
  title = ""
  for char in txt:
    if char.isalpha():
      title += char
      
  return title

