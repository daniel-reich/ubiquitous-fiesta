
def bitwise_index(lst):
 e = [i for i in lst if str(i)[len(str(i))-1] in list("02468")]
 if len(e) == 0:
  return "No even integer found!"
 else:
  em = (sorted(e))[len(e)-1]
  ind = [i for i in range(len(lst)) if lst[i] == em][0]
  if str(ind)[len(str(ind))-1] in list("02468"):
    return {"@even index "+str(ind): em}
  if str(ind)[len(str(ind))-1] in list("13579"):
    return {"@odd index "+str(ind): em}

