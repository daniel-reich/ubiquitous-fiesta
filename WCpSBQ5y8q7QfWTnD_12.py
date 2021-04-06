
def inflect(verb, person, number):
  base, ending = verb[:-3], verb[-3:]
  cat = ['are', 'ere', 'ire'].index(ending)
  pr, com = pronomi[person][number], verbi_com[person][number]
  spec = verbi_spec[person][number][cat]
  return ' '.join([pr, base + spec + com])

