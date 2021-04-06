
def inverter(txt, T):
  if T == 'P':
    return ' '.join(txt.split()[::-1]).capitalize()
  else:
    return ' '.join(w[::-1] for w in txt.split()).capitalize()

