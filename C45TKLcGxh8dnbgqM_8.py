
def caesar_cipher(s, k):
  output = ""
  for c in s:
    if c.isupper():
      output +=chr(((ord(c) + k - 65) % 26) + 65)
    elif c.islower():
      output += chr(((ord(c) + k - 97) % 26) + 97)
    else:
      output += c
  return output

