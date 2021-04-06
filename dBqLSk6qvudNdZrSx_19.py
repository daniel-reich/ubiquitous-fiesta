
def is_boiling(temp):
  return int(temp.replace("C","")) >= 100 if "C" in temp else int(temp.replace("F","")) >= 212 if "F" in temp else False

