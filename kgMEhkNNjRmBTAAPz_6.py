
def remove_special_characters(txt):
  special = set("!@#$%^&\'*().[]{}<>+=~,`|?")
  output = ''
  for char in txt:
    if char not in special:
      output += char
  return output

