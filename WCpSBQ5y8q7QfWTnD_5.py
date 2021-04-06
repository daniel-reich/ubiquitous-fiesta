
def inflect(verb,person,number):
  if "are" in verb:
    cl = 0
  elif "ere" in verb:
    cl = 1
  else:
    cl = 2
  subj = pronomi[person][number]
  verb = verb[:-3] + verbi_spec[person][number][cl] + verbi_com[person][number]
  return subj + " " + verb

