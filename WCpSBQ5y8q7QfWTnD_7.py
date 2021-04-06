
def inflect(verb, person, number):
  ret = pronomi[person][number]+' '+verb[:-3]
  if verb.endswith('are'):
    ret+=verbi_spec[person][number][0]+verbi_com[person][number]
  elif verb.endswith('ere'):
    ret+=verbi_spec[person][number][1]+verbi_com[person][number]
  elif verb.endswith('ire'):
    ret+=verbi_spec[person][number][2]+verbi_com[person][number]
  return ret

