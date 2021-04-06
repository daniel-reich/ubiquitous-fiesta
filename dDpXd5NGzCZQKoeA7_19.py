
def num_args(func):
  boucle = 1
  liste = []
  while boucle:
    try:
      func(*liste)
      return len(liste)
    except TypeError:
      liste.append(1)

