
def shift_letters(text, n):
  only_words = list(filter(lambda x : x.isalpha(), text))
  first_letter = only_words[-1]
  text = [i for i in text]
  
  for i in range(len(text)):
    if text[i] != " " and n != 0:
      text[i] = first_letter
      only_words = iter(only_words)
      first_letter = next(only_words)
      
  if n == 1 or n == 0:
    return "".join(text)
    
  return shift_letters("".join(text), n - 1)

