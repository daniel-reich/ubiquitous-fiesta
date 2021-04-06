
def mubashir_cipher(message):
  t1 = 'abcdefghijklmnopqrstuvwxyz'
  t2 = 'kgmqutbxzoancljwdyvfesphri'
  return message.translate(str.maketrans(t1, t2))

