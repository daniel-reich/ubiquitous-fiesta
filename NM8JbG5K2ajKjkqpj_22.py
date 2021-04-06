
def asc_des_none(lst, s):
  d = {"Asc": sorted(lst), "Des": sorted(lst, reverse=True), "None": lst}
  return d[s]

