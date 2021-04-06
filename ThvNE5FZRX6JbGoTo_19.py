
def inverter(txt, type):
  return ' '.join(i for i in txt.split()[::-1]).capitalize() if type == 'P' else ' '.join(i[::-1] for i in txt.split()).capitalize()

