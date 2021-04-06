
import numpy as np
import pandas as pd
def chi_squared_test(data):
  E2 = data['E'][0]
  E12 = data['E'][1]
  T2 = data['T'][0]
  T12 = data['T'][1]
  
  sum_E = E2 + E12
  sum_T = T2 + T12
  sum_2 = E2 + T2
  sum_12 = E12 + T12
  sum_all = sum_E + sum_T
  
  E2_exp = sum_E * sum_2 / sum_all
  E12_exp = sum_12 * sum_E / sum_all
  T2_exp = sum_2 * sum_T / sum_all
  T12_exp = sum_T * sum_12 / sum_all
  
  E2_final =  (E2 - E2_exp)**2 / E2_exp
  E12_final = (E12 - E12_exp)**2 / E12_exp
  T2_final = (T2 - T2_exp)**2 / T2_exp
  T12_final = (T12 - T12_exp)**2 / T12_exp#
  
  chi2 = round(E2_final + E12_final + T2_final + T12_final,1)
  
  alpha_1 = 6.635
  alpha_5 = 3.841
  
  res_string = ''
  
  if chi2 > alpha_1:
    res_string = "Edabitin effectiveness = 99%"
  else:
    if chi2 > alpha_5:
      res_string = "Edabitin effectiveness = 95%"
    else:
      res_string = "Edabitin is ininfluent"
  
  sol = [chi2, res_string]
  return sol

