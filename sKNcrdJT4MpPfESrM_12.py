
def remove_virus(f):
  r=[x for x in f.split()if'virus'not in x and'malware'not in x or'anti'in x or'not'in x]
  return' '.join(r).strip(',')if len(r)>2else'PC Files: Empty'

