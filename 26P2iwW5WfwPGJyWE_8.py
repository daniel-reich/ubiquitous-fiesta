
def possibly_perfect(key, answers):
  r=[True if i==h else "_" if i=="_" else False for i,h in zip(key,answers)]
  return True if all(r) or r.count(False)+r.count("_")==len(answers) else False

