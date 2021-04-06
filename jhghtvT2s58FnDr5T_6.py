
def jazzify(lst):
  concatenate = []
  for i in lst:
    if i[-1] == "7":
      concatenate.append(i)
    else:
      concatenate.append(i + "7")
  return concatenate

