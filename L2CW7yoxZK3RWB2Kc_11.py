
def nico_cipher(message, key):
  cipher = [[j,str(i)] for i, j in enumerate(key)]
  message += " "*(len(key)-len(message)%len(key))
  for i, j in enumerate(message):
    cipher[i%len(key)].append(j)
  cipher.sort()
  output = ""
  for i in range(2, len(cipher[0])):
    for j in cipher:
      output += j[i]
  return output

