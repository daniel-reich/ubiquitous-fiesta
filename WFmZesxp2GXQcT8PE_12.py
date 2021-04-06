
def digital_cipher(message, key):
  flst = []
  mlst = list(message)
  klst = [int(x) for x in str(key)]
  for a in range(len(mlst)):
    flst.append(ord(mlst[a]) - 96 + klst[a % len(klst)])
  return flst

