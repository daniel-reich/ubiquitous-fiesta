
d = {1:"Io",2:"Tu",3:"Egli", 4:"Noi",5:"Voi",6:"Essi"}
d2 = {"Io":"o","Tu":"i","Egli":"a","Noi":"iamo","Voi":"ate","Essi":"amo"}
def conjugate(verb, pronoun):
  v = verb[:-3]
  if v[-1] == "c" or v[-1] == "g":
    if pronoun == 2 or pronoun == 4:
      temp = v + "h"  + d2[d[pronoun]]
      final = d[pronoun] + " " + temp.lower()
  elif v[-1] == "i":
    if pronoun == 2 or pronoun == 4:
      temp = v[:-1]  + d2[d[pronoun]]
      final = d[pronoun] + " " + temp.lower()
    else:
      final = d[pronoun] + " " + v.lower() + d2[d[pronoun]]
  else:
    final = d[pronoun] + " " + v + d2[d[pronoun]]
  return final

