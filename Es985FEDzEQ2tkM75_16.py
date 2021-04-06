
def caesar_cipher(text, key):
  al = "abcdefghijklmnopqrstuvwxyz"
  return "".join(al[(al.find(lett)+key)%26] if lett!=" " else " " for lett in text)

