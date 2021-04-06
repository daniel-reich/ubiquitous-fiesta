
def digital_decipher(e, k):
  return "".join([chr(e[i] + 96 - int((str(k) * (i+1))[i])) for i in range(len(e))])

