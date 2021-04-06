
def clean_up_list(lst):
  lista = [[],[]]
  for num in lst:
    if int(num) % 2 == 0:
      lista[0].append(int(num))
    else:
      lista[1].append(int(num))
  return lista

