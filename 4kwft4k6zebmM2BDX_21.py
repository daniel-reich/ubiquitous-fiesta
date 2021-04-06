
def chi_squared_test(e_vs_t):
  import numpy as np
  outcomes = np.array([e_vs_t['E'], e_vs_t['T']])
  expected_values = np.array([[0.0, 0.0],[0.0, 0.0]])  
  chi_values = np.array([[0.0, 0.0],[0.0, 0.0]])
  for i in range(2):
    for j in range(2):
      expected_values[i, j] = (sum(outcomes[i, :]) * sum(outcomes[:, j])) / float(sum(sum(outcomes)))
  for i in range(2):
    for j in range(2):
      chi_values[i, j] = (outcomes[i, j] - expected_values[i, j])**2 / float(expected_values[i, j])
  chi = float(sum(sum(chi_values)))
  if chi < 3.841:
    return [round(chi, 1), "Edabitin is ininfluent"]
  elif sum(sum(chi_values)) > 6.635:
    return [round(chi, 1), "Edabitin effectiveness = 99%"]
  else:
    return [round(chi, 1), "Edabitin effectiveness = 95%"]

