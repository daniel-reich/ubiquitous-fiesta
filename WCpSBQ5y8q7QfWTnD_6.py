
def inflect(verb, person, number):
  return "{} {}{}{}".format(pronomi[person][number],
                            verb[:-3],
                            verbi_spec[person][number]["aei".find(verb[-3])],
                            verbi_com[person][number])

