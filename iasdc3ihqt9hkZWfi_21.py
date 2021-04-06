
def can_give_blood(donor, receiver):
  B={"O":"OAB","A":["A","AB"],"B":["B","AB"],"AB":["AB"]}
  return (donor[-1]=="-" or receiver[-1]=="+") and receiver[:-1] in B[donor[:-1]]

