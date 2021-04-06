
def dashed(txt):
  vowels = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}
  outputString = ""
  
  for char in txt:
    if (char in vowels): 
      outputString += "-" + char + "-"
    else: 
      outputString += char
    
  return outputString

