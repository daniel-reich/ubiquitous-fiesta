
def dif_ciph(inpt):
  if isinstance(inpt[0], str):
    return [ord(inpt[0])] + [ord(inpt[x]) - ord(inpt[x-1]) for x in range(1, len(inpt))]
  return chr(inpt[0]) + ''.join([chr(sum(inpt[:x+1]))for x in range(1, len(inpt))])

