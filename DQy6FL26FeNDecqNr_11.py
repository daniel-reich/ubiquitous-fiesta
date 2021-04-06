
def correct_stream(user, correct):
  lista = list()
  for i in range(len(user)):
    if user[i] == correct[i]:
      lista.append(1)
    else:
      lista.append(-1)
  return lista

