
def replace_vowels(txt, ch):
  exit_txt = ''
  for char in txt:
    if char in ['a', 'e', 'i', 'o', 'u']:
      exit_txt += ch
    else:
      exit_txt += char
    
  return exit_txt

