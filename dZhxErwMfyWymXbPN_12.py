
def hangman(phrase, lst):
  output = ''
  for i in phrase:
    if i.lower() in lst:
      output += i
    elif not i.isalpha():
      output += i
    else:
      output += '-'
  return output

