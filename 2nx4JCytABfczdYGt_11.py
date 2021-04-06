
def conjugate(verb, pronoun):
  def get_pronoun(num):
    prodict = {1 : "Io",2 : "Tu" ,3 : "Egli" ,4 : "Noi",5 : "Voi",6 : "Essi"}
    return prodict.get(num)
  def get_suffix(num):
    sufdict = {1 : "o",2 : "i" ,3 : "a" ,4 : "iamo",5 : "ate",6 : "ano"}
    return sufdict.get(num)
  body = verb[:-3]
  if body[-1] == "i":
    if pronoun == 2 or pronoun == 4:
      body = body[:-1]
  elif body[-1] == "g" or body[-1] == "c":
    if pronoun == 2 or pronoun == 4:
      body = body+"h"
  return "{} {}".format(get_pronoun(pronoun),body+get_suffix(pronoun))

