
def iso_group(lista_numeros):
​
  maximo = lista_numeros[0] #El maximo lo dejamos como el primero en la lista
  ultimo_elemento = lista_numeros[len(lista_numeros)-1]
  
  if ultimo_elemento > maximo:
    lista_numeros[0] = ultimo_elemento
  elif ultimo_elemento == maximo:
    lista_numeros.insert(0,ultimo_elemento)
  
  lista_numeros.pop()
​
  if todos_iguales(lista_numeros):
    if len(lista_numeros)>1:
      return lista_numeros
    else:
      return lista_numeros[0]
  return( iso_group(lista_numeros) )
​
def todos_iguales(lista):
  for i in range(1,len(lista)):
    if lista[i] != lista[i-1]:
      return(False)
  return(True)

