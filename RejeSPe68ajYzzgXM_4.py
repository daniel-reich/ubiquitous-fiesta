
def combine(lst):
  return {i[0]:[j[2] for j in lst if j[0]==i[0]] for i in lst}

