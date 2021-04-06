
def inator_inator(text):
  originalText = text
  vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  for v in vowels:
    if text[-1] == v:
      text += "-inator"
      text += " "
      text += str(len(originalText))
      text += "000"
      return text
  text += "inator"
  text += " "
  text += str(len(originalText))
  text += "000"
  return text

