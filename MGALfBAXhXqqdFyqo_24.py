
def atbash(txt):
  temp = ""
  for char in txt:
    if 65 <= ord(char) <= 90:
      char = 65 + (90 - ord(char))
      temp += chr(char) 
    elif 97 <= ord(char) <= 122:
      char = 97 + (122 - ord(char))
      temp += chr(char) 
    else:
      temp += char
  return temp

