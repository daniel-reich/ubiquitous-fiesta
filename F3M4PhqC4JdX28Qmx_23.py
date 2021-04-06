
def back_to_home(d):
  return (max(d.count("S"),d.count("N"))-min(d.count("S"),d.count("N")))+(max(d.count("W"),d.count("E"))-min(d.count("W"),d.count("E")))==0

