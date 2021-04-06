
def mubashir_cipher(message):
  alphabet='abcdefghijklmnopqrstuvwxyz'
  encryption ='kgmqutbxzoancljwdyvfesphri'
  result = message.maketrans(alphabet,encryption)
  result = message.translate(result)
  return result

