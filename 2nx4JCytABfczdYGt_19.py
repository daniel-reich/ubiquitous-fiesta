
def conjugate(verb, pronoun):
  verb = verb.replace("are", "")
  if pronoun == 1:
    verb = "Io " + verb + "o"
  if pronoun == 2:
    if verb[-1] == "i":
      verb = "Tu " + verb
    elif verb[-1] == "c" or verb[-1] == "g":
      verb = "Tu " + verb + "hi"
    else:
      verb = "Tu " + verb + "i"
  if pronoun == 3:
    verb = "Egli " + verb + "a"
  if pronoun == 4:
    if verb[-1] == "i":
      verb = "Noi " + verb + "amo"
    elif verb[-1] == "c" or verb[-1] == "g":
      verb = "Noi " + verb + "hiamo"
    else:
      verb = "Noi " + verb + "iamo"
  if pronoun == 5:
    verb = "Voi " + verb + "ate"
  if pronoun == 6:
    verb = "Essi " + verb + "ano"
​
  return verb

