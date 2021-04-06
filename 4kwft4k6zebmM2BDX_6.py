
def chi_squared_test(data):
  edabitin_total = data["E"][0] + data["E"][1]
  tutorial_total = data["T"][0] + data["T"][1]
  two_hr_total = data["E"][0] + data["T"][0]
  half_hr_total = data["E"][1] + data["T"][1]
  total = edabitin_total + tutorial_total
​
  edabitin_2hr_chi = (data["E"][0] - edabitin_total * two_hr_total / total)**2 / (edabitin_total * two_hr_total / total)
  edabitin_half_hr_chi = (data["E"][1] - edabitin_total * half_hr_total / total)**2 / (edabitin_total * half_hr_total / total)
  tutorial_2hr_chi = (data["T"][0] - tutorial_total * two_hr_total / total)**2 / (tutorial_total * two_hr_total / total)
  tutorial_half_hr_chi = (data["T"][1] - tutorial_total * half_hr_total / total)**2 / (tutorial_total * half_hr_total / total)
  chi_value = edabitin_2hr_chi + edabitin_half_hr_chi + tutorial_2hr_chi + \
  tutorial_half_hr_chi
  chi_value = round(chi_value, 1)
​
  ALPHA1 = 6.635
  ALPHA5 = 3.841
​
  if chi_value < ALPHA1 and chi_value > ALPHA5:
    return [chi_value, "Edabitin effectiveness = 95%"]
  else:
      if chi_value > ALPHA1:
        return [chi_value, "Edabitin effectiveness = 99%"]
      elif chi_value < ALPHA5:
        return [chi_value, "Edabitin is ininfluent"]

