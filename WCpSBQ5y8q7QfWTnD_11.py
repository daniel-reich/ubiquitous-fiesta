
def inflect(verb, person, number):
  verb_dict = {"a":0, "e":1, "i":2}
  letter = verb[-3]
  idx = verb_dict[letter]
  
  partial = verb[:-3]
  pron = pronomi[person][number]
  spec = verbi_spec[person][number][idx]
  com = verbi_com[person][number]
  
  return " ".join([pron, partial + spec + com])
  # return " ".join([pronomi[person][number], partial + verbi_spec[person][number] + verbi_com[person][number]])

