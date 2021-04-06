
def chi_squared_test(data):
  e = data["E"]
  t = data["T"]
  alpha = ""
  
  two_hr = e[0] + t[0]
  half_hr = e[1] + t[1]
  e_tot = e[0] + e[1]
  t_tot = t[0] + t[1]
  two_half_tot = two_hr + half_hr
  
  expected_2e = two_hr*e_tot / two_half_tot
  expected_halfe = half_hr*e_tot / two_half_tot
  expected_2t = two_hr*t_tot / two_half_tot
  expected_halft = half_hr * t_tot / two_half_tot
  
  s2e = (e[0] - expected_2e)**2 / expected_2e
  s12e = (e[1] - expected_halfe)**2 / expected_halfe
  s2t = (t[0] - expected_2t)**2 / expected_2t
  s12t = (t[1] - expected_halft)**2 / expected_halft
  
  sum = s2e + s12e + s2t + s12t
  
  if sum > 6.635:
    alpha = "Edabitin effectiveness = 99%"
  elif sum < 6.635 and sum > 3.841:
    alpha = "Edabitin effectiveness = 95%"
  else:
    alpha = "Edabitin is ininfluent"
    
  return_list = [round(sum,1),alpha]
  return return_list

