
def replace_the(txt):
  vowels="aeiou"
  text=txt.split()
  for i in range(len(text)):
    if text[i]=="the":
      if text[i+1][0] in vowels:
        text[i]="an"
      else:
        text[i]="a"
  return " ".join(text)

