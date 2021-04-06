
def mirror_cipher(*message):
  import string
  try:
    txt, key = message
  except ValueError:
    txt = message[0]
    key = string.ascii_lowercase
  txt = txt.lower()
  trantab = txt.maketrans(key, key[::-1])
  return txt.translate(trantab)

