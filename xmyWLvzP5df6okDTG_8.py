
def binary_to_decimal(binary):
  indice=0
  binary=binary[::-1]
  suma=0
  for x in binary:
    if x==1:
      suma=suma+2**indice
      indice=indice+1
    else:
      indice=indice+1
  return suma

