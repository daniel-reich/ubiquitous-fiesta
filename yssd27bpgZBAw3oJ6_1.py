
def probability(u):
  prob_not = 1
  for person in range(2, u + 1):
    prob_not *= (364-(person - 2)) / 365
    
  return round(1 - prob_not, 2)

