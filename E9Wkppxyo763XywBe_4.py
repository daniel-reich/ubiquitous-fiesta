
def binary_clock(time):
  time = time.split(":")
  tamanho_max = [2, 4, 3, 4, 3, 4]
  cont = 0
  numeros = []
​
  for digitos in time:
      for digito in digitos:
          binario = (bin(int(digito))[2:])
          if len(binario) < tamanho_max[cont]:
              remaining = tamanho_max[cont] - len(binario)
              # print(remaining)
              binario = (remaining*"0")+str(binario)
              binario = str(binario)
              numeros.append(binario)
          else:
              binario = str(binario)
              numeros.append(binario)
          cont += 1
  # print(numeros)
​
  h1, h2, m1, m2, s1, s2 = numeros
​
  def inverter(h1, h2, m1, m2, s1, s2):
      return [
          " "+h2[0]+" "+m2[0]+" "+s2[0],
          " "+h2[1]+m1[0]+m2[1]+s1[0]+s2[1],
          h1[0]+h2[2]+m1[1]+m2[2]+s1[1]+s2[2],
          h1[1]+h2[3]+m1[2]+m2[3]+s1[2]+s2[3]
      ]
  
  return(inverter(h1, h2, m1, m2, s1, s2))

