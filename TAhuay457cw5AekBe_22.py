
def monkey_talk(txt):
  vowels = 'aeiou'
  words = txt.split()
  output = ""
  for word in words:
    if word[0].lower() in vowels:
      output += "eek "
    else:
      output += "ook "
  output = output[0].upper()+output[1:-1]+"."
  return output

