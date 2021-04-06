
def words_to_sentence(words):
  if words==[]:
    return ""
  elif words==None:
    return ""
  nwords = [i for i in words if i!=""]
  if len(nwords)>1:
    return ", ".join(nwords[:-1])+" and "+nwords[-1]
  else:
    return "".join(nwords)

