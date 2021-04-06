
def print_all_groups():
  lista=[]
  for x in range (1,7):
    for j in "abcde":
      lista.append(str(x)+j)
  return ", ".join(lista)

