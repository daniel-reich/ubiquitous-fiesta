
def index_of_caps(word):
  liste = []
  for i, j in enumerate(word):
    if j.isupper() == True:
      liste.append(i)
  return liste

