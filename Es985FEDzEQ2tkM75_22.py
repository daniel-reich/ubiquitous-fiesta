
def caesar_cipher(text, key):
  result = ""
  for i in text:
    if i == " ":
      result+= " "
    elif i.isupper():
      result+= chr((ord(i)+key-65)%26+65)
    else:
      result+= chr((ord(i)+key-97)%26+97)
  return result

